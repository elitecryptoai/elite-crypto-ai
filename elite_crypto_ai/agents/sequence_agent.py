# sequence_agent.py — ULTRA ELITE PIPELINE RUNNER

import subprocess

AGENTS = [
    "price_feed_agent.py",
    "search_agent.py",
    "coin_generator.py",
    "symbol_mapper.py",
    "analytics_agent.py",
    "intel_engine.py",
    "forecast_agent.py",
    "forecast_accuracy_tracker.py",
    "forecast_memory_logger.py",
    "strategy_generator_agent.py",
    "strategy_agent.py",
    "strategy_simulator.py",
    "strategy_heatmap_generator.py",
    "strategy_batch_runner.py",
    "strategy_tracker.py",
    "rebalancer_agent.py",
    "manager_agent.py",
    "execution_agent.py",
    "report_builder.py",
    "dashboard_agent.py",
    "email_reporter.py",
    "model_rank_updater.py",
    "self_trainer.py",
    "agent_auto_regen.py",
    "uniswap_router.py",
    "source_manager.py"
]

def run_agents():
    print("▶️ Initiating full ultra elite sequence pipeline...\n")
    for agent in AGENTS:
        print(f"▶️ Running: {agent}")
        try:
            subprocess.run(["python3", f"agents/{agent}"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ {agent} failed with error: {e}\n")
        print()

if __name__ == "__main__":
    run_agents()
