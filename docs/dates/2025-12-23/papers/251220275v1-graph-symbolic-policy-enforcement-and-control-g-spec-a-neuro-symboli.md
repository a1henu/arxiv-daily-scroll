---
layout: default
title: Graph-Symbolic Policy Enforcement and Control (G-SPEC): A Neuro-Symbolic Framework for Safe Agentic AI in 5G Autonomous Networks
---

# Graph-Symbolic Policy Enforcement and Control (G-SPEC): A Neuro-Symbolic Framework for Safe Agentic AI in 5G Autonomous Networks
**arXiv**：[2512.20275v1](https://arxiv.org/abs/2512.20275) · [PDF](https://arxiv.org/pdf/2512.20275.pdf)  
**作者**：Divya Vijay, Vignesh Ethiraj  

**一句话要点**：提出G-SPEC神经符号框架，以解决5G自主网络中LLM代理的安全风险问题。

**关键词**：神经符号框架, 5G自主网络, 政策强制执行, 网络知识图谱, SHACL约束, 安全代理AI

## 3 点简述
- 核心问题：5G/6G网络自动化中，LLM代理存在拓扑幻觉和政策违规等随机风险。
- 方法要点：结合概率规划和确定性验证，通过治理三元组（TSLAM-4B代理、网络知识图谱、SHACL约束）强制执行政策。
- 实验或效果：在模拟450节点5G核心测试中，实现零安全违规和94.1%修复成功率，验证延迟随子图大小呈O(k^1.2)缩放。

## 摘要（原文）

> As networks evolve toward 5G Standalone and 6G, operators face orchestration challenges that exceed the limits of static automation and Deep Reinforcement Learning. Although Large Language Model (LLM) agents offer a path toward intent-based networking, they introduce stochastic risks, including topology hallucinations and policy non-compliance. To mitigate this, we propose Graph-Symbolic Policy Enforcement and Control (G-SPEC), a neuro-symbolic framework that constrains probabilistic planning with deterministic verification. The architecture relies on a Governance Triad - a telecom-adapted agent (TSLAM-4B), a Network Knowledge Graph (NKG), and SHACL constraints. We evaluated G-SPEC on a simulated 450-node 5G Core, achieving zero safety violations and a 94.1% remediation success rate, significantly outperforming the 82.4% baseline. Ablation analysis indicates that NKG validation drives the majority of safety gains (68%), followed by SHACL policies (24%). Scalability tests on topologies ranging from 10K to 100K nodes demonstrate that validation latency scales as $O(k^{1.2})$ where $k$ is subgraph size. With a processing overhead of 142ms, G-SPEC is viable for SMO-layer operations.

