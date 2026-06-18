const GemmaOS = {
    state: {
        npu_load: 18,
        mem_used: 4.2,
        batt_level: 92,
        active_agents: ["Device", "Security", "Coding"],
        user_state: "Deep Work",
        threats: 0,
        patterns_discovered: 12,
        is_listening: false,
        personality: "Professional"
    },

    init() {
        setInterval(() => {
            this.state.npu_load = Math.floor(15 + Math.random() * 10);
            this.updateUI();
        }, 3000);
        this.updateUI();
        this.log("Kernel: AI Resource Scheduler initialized.");
        this.log("Runtime: Gemma 4 E2B-it loaded on NPU.");
    },

    updateUI() {
        // Status bars
        document.querySelectorAll('.status-bar span:nth-child(1)').forEach(el => {
            if (el.innerText.includes("NPU")) el.innerText = `NPU ${this.state.npu_load}%`;
        });

        // Agent lists
        const agentList = document.querySelector('.agent-list');
        if (agentList) {
            agentList.innerHTML = this.state.active_agents.map(a => `<li>${a} Agent</li>`).join('');
        }
    },

    log(msg) {
        const consoleOut = document.getElementById('console-output');
        if (consoleOut) {
            const time = new Date().toLocaleTimeString();
            consoleOut.innerHTML += `<div>[${time}] ${msg}</div>`;
            consoleOut.scrollTop = consoleOut.scrollHeight;
        }
    },

    toggleConsole() {
        const consoleEl = document.getElementById('system-console');
        consoleEl.style.display = consoleEl.style.display === 'none' ? 'block' : 'none';
    },

    setSetting(key, value) {
        this.state[key] = value;
        this.log(`Settings: Updated ${key} to ${value}`);
    },

    dispatchIntent(intent) {
        this.log(`Orchestrator: Decomposing intent '${intent}'...`);
        setTimeout(() => {
            this.log("Agent Swarm: Task completed successfully.");
        }, 1500);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    GemmaOS.init();
    // Enable system console via hotkey (Ctrl+`)
    document.addEventListener('keydown', (e) => {
        if (e.key === '`' && e.ctrlKey) GemmaOS.toggleConsole();
    });
});

// Studio Controls
const StudioControl = {
    generate(type, prompt) {
        GemmaOS.log(`[CREATOR] Initiating ${type} generation: ${prompt}`);
    },
    scaffoldApp(prompt) {
        GemmaOS.log(`[APP BUILDER] Scaffolding Jetpack Compose project: ${prompt}`);
    },
    runResearch(topic) {
        GemmaOS.log(`[RESEARCH] Analyzing vault for topic: ${topic}`);
    }
};
