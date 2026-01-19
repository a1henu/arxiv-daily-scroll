---
layout: default
title: Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs
---

# Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs
**arXiv**：[2601.11061v1](https://arxiv.org/abs/2601.11061) · [PDF](https://arxiv.org/pdf/2601.11061.pdf)  
**作者**：Lecheng Yan, Ruizhe Li, Guanhua Chen, Qing Li, Jiahui Geng, Wenxi Li, Vincent Wang, Chris Lee  

**一句话要点**：揭示RLVR中虚假奖励激活记忆捷径的机制，提供缓解数据污染的路线图

**关键词**：强化学习验证奖励, 记忆捷径, 数据污染, 机制解释, 因果分析, 大语言模型

## 3 点简述
- 核心问题：虚假奖励导致LLM绕过推理，依赖记忆捷径，引发困惑度悖论
- 方法要点：使用路径修补、Logit Lens、JSD分析和神经微分方程定位锚点-适配器电路
- 实验或效果：在Qwen 2.5模型中识别中间层锚点和后期适配器，通过缩放MLP键实现双向因果操控

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) is highly effective for enhancing LLM reasoning, yet recent evidence shows models like Qwen 2.5 achieve significant gains even with spurious or incorrect rewards. We investigate this phenomenon and identify a "Perplexity Paradox": spurious RLVR triggers a divergence where answer-token perplexity drops while prompt-side coherence degrades, suggesting the model is bypassing reasoning in favor of memorization. Using Path Patching, Logit Lens, JSD analysis, and Neural Differential Equations, we uncover a hidden Anchor-Adapter circuit that facilitates this shortcut. We localize a Functional Anchor in the middle layers (L18-20) that triggers the retrieval of memorized solutions, followed by Structural Adapters in later layers (L21+) that transform representations to accommodate the shortcut signal. Finally, we demonstrate that scaling specific MLP keys within this circuit allows for bidirectional causal steering-artificially amplifying or suppressing contamination-driven performance. Our results provide a mechanistic roadmap for identifying and mitigating data contamination in RLVR-tuned models. Code is available at https://github.com/idwts/How-RLVR-Activates-Memorization-Shortcuts.

