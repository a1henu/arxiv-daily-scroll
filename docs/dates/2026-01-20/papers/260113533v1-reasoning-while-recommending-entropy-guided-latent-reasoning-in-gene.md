---
layout: default
title: Reasoning While Recommending: Entropy-Guided Latent Reasoning in Generative Re-ranking Models
---

# Reasoning While Recommending: Entropy-Guided Latent Reasoning in Generative Re-ranking Models
**arXiv**：[2601.13533v1](https://arxiv.org/abs/2601.13533) · [PDF](https://arxiv.org/pdf/2601.13533.pdf)  
**作者**：Changshuo Zhang  

**一句话要点**：提出熵引导隐式推理模型，在生成式重排序中实现实时推理以提升推荐精度

**关键词**：生成式重排序, 隐式推理, 熵引导, 强化学习, 列表生成, 实时推理

## 3 点简述
- 核心问题：现有生成式重排序方法难以适应列表生成中模型难度的动态熵变化，影响复杂偏好捕获
- 方法要点：引入隐式推理机制，通过上下文感知推理令牌和动态温度调整实现熵引导变长推理
- 实验或效果：在真实数据集上验证有效性，兼容现有模型提升性能，具有部署价值和研究潜力

## 摘要（原文）

> Reinforcement learning plays a crucial role in generative re-ranking scenarios due to its exploration-exploitation capabilities, but existing generative methods mostly fail to adapt to the dynamic entropy changes in model difficulty during list generation, making it challenging to accurately capture complex preferences. Given that language models have achieved remarkable breakthroughs by integrating reasoning capabilities, we draw on this approach to introduce a latent reasoning mechanism, and experimental validation demonstrates that this mechanism effectively reduces entropy in the model's decision-making process. Based on these findings, we introduce the Entropy-Guided Latent Reasoning (EGLR) recommendation model, which has three core advantages. First, it abandons the "reason first, recommend later" paradigm to achieve "reasoning while recommending", specifically designed for the high-difficulty nature of list generation by enabling real-time reasoning during generation. Second, it implements entropy-guided variable-length reasoning using context-aware reasoning token alongside dynamic temperature adjustment, expanding exploration breadth in reasoning and boosting exploitation precision in recommending to achieve a more precisely adapted exploration-exploitation trade-off. Third, the model adopts a lightweight integration design with no complex independent modules or post-processing, enabling easy adaptation to existing models. Experimental results on two real-world datasets validate the model's effectiveness, and its notable advantage lies in being compatible with existing generative re-ranking models to enhance their performance. Further analyses also demonstrate its practical deployment value and research potential.

