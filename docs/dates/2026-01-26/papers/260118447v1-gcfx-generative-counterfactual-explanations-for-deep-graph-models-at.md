---
layout: default
title: GCFX: Generative Counterfactual Explanations for Deep Graph Models at the Model Level
---

# GCFX: Generative Counterfactual Explanations for Deep Graph Models at the Model Level
**arXiv**：[2601.18447v1](https://arxiv.org/abs/2601.18447) · [PDF](https://arxiv.org/pdf/2601.18447.pdf)  
**作者**：Jinlong Hu, Jiacheng Liu  

**一句话要点**：提出GCFX方法，基于深度图生成，为深度图模型提供模型级反事实解释。

**关键词**：深度图学习, 反事实解释, 模型级解释, 图生成, 全局预测模式, 透明度增强

## 3 点简述
- 核心问题：深度图模型内部复杂且不透明，难以解释其决策，影响用户理解与信任。
- 方法要点：结合双编码器、结构感知标记器和MPNN解码器，生成高质量反事实示例，并通过全局总结算法选取代表性解释。
- 实验或效果：在合成和真实数据集上，GCFX在反事实有效性和覆盖范围上优于现有方法，且解释成本低。

## 摘要（原文）

> Deep graph learning models have demonstrated remarkable capabilities in processing graph-structured data and have been widely applied across various fields. However, their complex internal architectures and lack of transparency make it difficult to explain their decisions, resulting in opaque models that users find hard to understand and trust. In this paper, we explore model-level explanation techniques for deep graph learning models, aiming to provide users with a comprehensive understanding of the models' overall decision-making processes and underlying mechanisms. Specifically, we address the problem of counterfactual explanations for deep graph learning models by introducing a generative model-level counterfactual explanation approach called GCFX, which is based on deep graph generation. This approach generates a set of high-quality counterfactual explanations that reflect the model's global predictive behavior by leveraging an enhanced deep graph generation framework and a global summarization algorithm. GCFX features an architecture that combines dual encoders, structure-aware taggers, and Message Passing Neural Network decoders, enabling it to accurately learn the true latent distribution of input data and generate high-quality, closely related counterfactual examples. Subsequently, a global counterfactual summarization algorithm selects the most representative and comprehensive explanations from numerous candidate counterfactuals, providing broad insights into the model's global predictive patterns. Experiments on a synthetic dataset and several real-world datasets demonstrate that GCFX outperforms existing methods in terms of counterfactual validity and coverage while maintaining low explanation costs, thereby offering crucial support for enhancing the practicality and trustworthiness of global counterfactual explanations.

