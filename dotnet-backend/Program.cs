using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using predictive_climate_control.Communication;
using predictive_climate_control.Services;
using predictive_climate_control.Streaming;

var builder = WebApplication.CreateBuilder(args);

// configure services
var aiServiceUrl = builder.Configuration["AiService:BaseUrl"] ?? "http://localhost:8000";
builder.Services.AddHttpClient<ClimateOptimizationService>(client =>
{
    client.BaseAddress = new Uri(aiServiceUrl);
    client.Timeout = TimeSpan.FromSeconds(10);
});
builder.Services.AddSingleton<CanBusInterface>();
builder.Services.AddSingleton<HvacController>();
builder.Services.AddSingleton<WebSocketService>();
builder.Services.AddSingleton<TelemetryService>();

builder.Services.AddCors(options =>
{
    var origins = builder.Configuration.GetSection("Cors:AllowedOrigins").Get<string[]>()
        ?? new[] { "http://localhost:3000" };
    options.AddDefaultPolicy(policy => policy.WithOrigins(origins).AllowAnyHeader().AllowAnyMethod());
});

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}
app.UseCors();
app.UseWebSockets();

// dashboard clients subscribe here for live telemetry
app.Map("/ws/telemetry", async context =>
{
    if (!context.WebSockets.IsWebSocketRequest)
    {
        context.Response.StatusCode = StatusCodes.Status400BadRequest;
        return;
    }
    using var socket = await context.WebSockets.AcceptWebSocketAsync();
    await context.RequestServices.GetRequiredService<WebSocketService>()
        .HandleClientAsync(socket, context.RequestAborted);
});

app.MapControllers();

app.Run();
