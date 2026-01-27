---
layout: default
title: $α^3$-SecBench: A Large-Scale Evaluation Suite of Security, Resilience, and Trust for LLM-based UAV Agents over 6G Networks
---

# $α^3$-SecBench: A Large-Scale Evaluation Suite of Security, Resilience, and Trust for LLM-based UAV Agents over 6G Networks
**arXiv**：[2601.18754v1](https://arxiv.org/abs/2601.18754) · [PDF](https://arxiv.org/pdf/2601.18754.pdf)  
**作者**：Mohamed Amine Ferrag, Abderrahmane Lakas, Merouane Debbah  

**一句话要点**：提出α³-SecBench评估套件，用于测试基于LLM的无人机代理在6G网络下的安全、韧性和信任能力。

**关键词**：无人机安全评估, LLM代理测试, 6G网络韧性, 对抗攻击场景, 自主系统信任

## 3 点简述
- 核心问题：现有基准缺乏对基于LLM的无人机代理在对抗条件下的安全、韧性和信任的系统评估。
- 方法要点：基于α³-Bench，扩展20,000个攻击场景，覆盖七个自主层，评估安全、韧性和信任三个维度。
- 实验或效果：评估23个LLM，整体得分12.9%至57.1%，显示异常检测与安全决策间存在显著差距。

## 摘要（原文）

> Autonomous unmanned aerial vehicle (UAV) systems are increasingly deployed in safety-critical, networked environments where they must operate reliably in the presence of malicious adversaries. While recent benchmarks have evaluated large language model (LLM)-based UAV agents in reasoning, navigation, and efficiency, systematic assessment of security, resilience, and trust under adversarial conditions remains largely unexplored, particularly in emerging 6G-enabled settings.
>   We introduce $α^{3}$-SecBench, the first large-scale evaluation suite for assessing the security-aware autonomy of LLM-based UAV agents under realistic adversarial interference. Building on multi-turn conversational UAV missions from $α^{3}$-Bench, the framework augments benign episodes with 20,000 validated security overlay attack scenarios targeting seven autonomy layers, including sensing, perception, planning, control, communication, edge/cloud infrastructure, and LLM reasoning. $α^{3}$-SecBench evaluates agents across three orthogonal dimensions: security (attack detection and vulnerability attribution), resilience (safe degradation behavior), and trust (policy-compliant tool usage).
>   We evaluate 23 state-of-the-art LLMs from major industrial providers and leading AI labs using thousands of adversarially augmented UAV episodes sampled from a corpus of 113,475 missions spanning 175 threat types. While many models reliably detect anomalous behavior, effective mitigation, vulnerability attribution, and trustworthy control actions remain inconsistent. Normalized overall scores range from 12.9% to 57.1%, highlighting a significant gap between anomaly detection and security-aware autonomous decision-making. We release $α^{3}$-SecBench on GitHub: https://github.com/maferrag/AlphaSecBench

