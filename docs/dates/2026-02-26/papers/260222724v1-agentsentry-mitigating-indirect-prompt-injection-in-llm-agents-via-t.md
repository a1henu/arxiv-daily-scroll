---
layout: default
title: AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification
---

# AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification
**arXiv**：[2602.22724v1](https://arxiv.org/abs/2602.22724) · [PDF](https://arxiv.org/pdf/2602.22724.pdf)  
**作者**：Tian Zhang, Yiwei Xu, Juan Wang, Keyan Guo, Xiaoyang Xu, Bowen Xiao, Quanlong Guan, Jinlin Fan, Jiawei Liu, Zhiquan Liu, Hongxin Hu  

**一句话要点**：提出AgentSentry以缓解LLM代理中的间接提示注入攻击

**关键词**：间接提示注入, LLM代理安全, 时间因果诊断, 上下文净化, 推理时防御

## 3 点简述
- 核心问题：LLM代理在多轮交互中易受间接提示注入攻击，现有防御方法易误判或中断任务。
- 方法要点：通过时间因果诊断定位攻击点，并利用因果引导的上下文净化安全继续执行。
- 实验或效果：在AgentDojo基准测试中消除攻击，保持高实用性和良性性能。

## 摘要（原文）

> Large language model (LLM) agents increasingly rely on external tools and retrieval systems to autonomously complete complex tasks. However, this design exposes agents to indirect prompt injection (IPI), where attacker-controlled context embedded in tool outputs or retrieved content silently steers agent actions away from user intent. Unlike prompt-based attacks, IPI unfolds over multi-turn trajectories, making malicious control difficult to disentangle from legitimate task execution. Existing inference-time defenses primarily rely on heuristic detection and conservative blocking of high-risk actions, which can prematurely terminate workflows or broadly suppress tool usage under ambiguous multi-turn scenarios. We propose AgentSentry, a novel inference-time detection and mitigation framework for tool-augmented LLM agents. To the best of our knowledge, AgentSentry is the first inference-time defense to model multi-turn IPI as a temporal causal takeover. It localizes takeover points via controlled counterfactual re-executions at tool-return boundaries and enables safe continuation through causally guided context purification that removes attack-induced deviations while preserving task-relevant evidence. We evaluate AgentSentry on the \textsc{AgentDojo} benchmark across four task suites, three IPI attack families, and multiple black-box LLMs. AgentSentry eliminates successful attacks and maintains strong utility under attack, achieving an average Utility Under Attack (UA) of 74.55 %, improving UA by 20.8 to 33.6 percentage points over the strongest baselines without degrading benign performance.

