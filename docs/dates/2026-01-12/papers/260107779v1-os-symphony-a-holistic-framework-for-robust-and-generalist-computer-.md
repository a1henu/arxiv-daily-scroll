---
layout: default
title: OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agent
---

# OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agent
**arXiv**：[2601.07779v1](https://arxiv.org/abs/2601.07779) · [PDF](https://arxiv.org/pdf/2601.07779.pdf)  
**作者**：Bowen Yang, Kaiming Jin, Zhenyu Wu, Zhaoyang Liu, Qiushi Sun, Zehao Li, JingJing Xie, Zhoumianze Liu, Fangzhi Xu, Kanzhi Cheng, Qingyun Li, Yian Wang, Yu Qiao, Zun Wang, Zichen Ding  

**一句话要点**：提出OS-Symphony框架以解决计算机使用代理在长流程任务中的鲁棒性和新领域泛化问题

**关键词**：计算机使用代理, 长流程任务, 视觉语言模型, 鲁棒性框架, 教程检索, 在线基准测试

## 3 点简述
- 核心问题：现有框架在长流程任务中视觉上下文控制不足，缺乏视觉感知的教程检索，导致鲁棒性和泛化性差
- 方法要点：引入Orchestrator协调反思记忆代理和多功能工具代理，通过里程碑驱动记忆和SeeAct范式合成视觉对齐教程
- 实验或效果：在三个在线基准测试中取得新SOTA，OSWorld上达到65.84%，不同模型规模下性能显著提升

## 摘要（原文）

> While Vision-Language Models (VLMs) have significantly advanced Computer-Using Agents (CUAs), current frameworks struggle with robustness in long-horizon workflows and generalization in novel domains. These limitations stem from a lack of granular control over historical visual context curation and the absence of visual-aware tutorial retrieval. To bridge these gaps, we introduce OS-Symphony, a holistic framework that comprises an Orchestrator coordinating two key innovations for robust automation: (1) a Reflection-Memory Agent that utilizes milestone-driven long-term memory to enable trajectory-level self-correction, effectively mitigating visual context loss in long-horizon tasks; (2) Versatile Tool Agents featuring a Multimodal Searcher that adopts a SeeAct paradigm to navigate a browser-based sandbox to synthesize live, visually aligned tutorials, thereby resolving fidelity issues in unseen scenarios. Experimental results demonstrate that OS-Symphony delivers substantial performance gains across varying model scales, establishing new state-of-the-art results on three online benchmarks, notably achieving 65.84% on OSWorld.

