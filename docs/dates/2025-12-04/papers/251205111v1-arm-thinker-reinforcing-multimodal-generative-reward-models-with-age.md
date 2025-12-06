---
layout: default
title: ARM-Thinker: Reinforcing Multimodal Generative Reward Models with Agentic Tool Use and Visual Reasoning
---

# ARM-Thinker: Reinforcing Multimodal Generative Reward Models with Agentic Tool Use and Visual Reasoning
**arXiv**：[2512.05111v1](https://arxiv.org/abs/2512.05111) · [PDF](https://arxiv.org/pdf/2512.05111.pdf)  
**作者**：Shengyuan Ding, Xinyu Fang, Ziyu Liu, Yuhang Zang, Yuhang Cao, Xiangyu Zhao, Haodong Duan, Xiaoyi Dong, Jianze Liang, Bin Wang, Conghui He, Dahua Lin, Jiaqi Wang  

**一句话要点**：提出ARM-Thinker，通过代理工具使用增强多模态奖励模型，解决视觉幻觉和验证不足问题。

**关键词**：多模态奖励模型, 代理工具使用, 视觉推理, 强化学习, 基准评估

## 3 点简述
- 当前奖励模型存在幻觉、视觉基础弱和无法使用工具验证的问题。
- ARM-Thinker自主调用外部工具进行证据验证，采用多阶段强化学习联合优化。
- 在ARMBench-VL基准上平均提升16.2%，工具使用任务提升9.6%。

## 摘要（原文）

> Reward models are critical for aligning vision-language systems with human preferences, yet current approaches suffer from hallucination, weak visual grounding, and an inability to use tools for verification, limiting their reliability on complex multimodal reasoning tasks. We present ARM-Thinker, an A}gentic multimodal Reward Model that autonomously invokes external tools (e.g., image cropping, doc page retrieval) to ground judgments in verifiable evidence, replacing static, non-interactive reward scoring. This enables the model to verify fine-grained visual details, cross-reference multi-page evidence, and validate reasoning claims, which are capabilities absent in existing reward models. We train ARM-Thinker with multi-stage reinforcement learning, jointly optimizing tool-calling decisions and judgment accuracy. To evaluate agentic reward modeling, we introduce ARMBench-VL, comprising three benchmarks that assess fine-grained visual grounding (image-level tools), multi-page document understanding (retrieval tools), and instruction following (text-level verification). ARM-Thinker achieves +16.2% average improvement on reward modeling benchmarks, +9.6% on tool-use tasks, and outperforms baselines on multimodal math and logical reasoning benchmarks. Our results demonstrate that agentic capabilities significantly enhance both accuracy and interpretability of reward models.

