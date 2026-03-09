# Simulation-of-phishing-attack-This project is a specialized web application developed as part of a Bachelor’s thesis to analyze the psychological and technical aspects of phishing attacks. Unlike standard simulation tools, this platform focuses on the Human-in-the-Loop vulnerability by measuring user response times and cognitive processing under pressure.

Core Components & Functionalities:

    Social Engineering Simulation: A high-fidelity email and landing page replica that utilizes psychological triggers such as Urgency (Scarcity) and Authority (Halo Effect) to bypass analytical thinking.

    Latency Tracking (Cognitive Load Measurement): Implemented a custom backend logic in Flask to measure the exact duration between page access and data submission. This metric serves as a proxy for determining whether the user relied on System 1 (Intuitive) or System 2 (Analytical) thinking.

    Heuristic URL Analyzer: A dedicated security module that evaluates URL structures for common deception techniques, including Typosquatting (Homographs), excessive subdomains, and protocol inconsistencies (HTTP vs. HTTPS).

    Educational Feedback Loop: An immediate post-simulation results page that deconstructs the attack vectors, providing users with a "digital vaccine" effect by highlighting their specific reaction time and the psychological traps they encountered.
