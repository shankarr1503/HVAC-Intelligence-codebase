using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using predictive_climate_control.Services;

var builder = WebApplication.CreateBuilder(args);

// configure services
builder.Services.AddSingleton<ClimateOptimizationService>();
builder.Services.AddSingleton<HvacController>();
builder.Services.AddSingleton<TelemetryService>();

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}
app.MapControllers();

app.Run();
