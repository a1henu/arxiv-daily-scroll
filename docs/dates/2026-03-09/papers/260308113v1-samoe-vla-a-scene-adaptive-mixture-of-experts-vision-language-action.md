---
layout: default
title: SAMoE-VLA: A Scene Adaptive Mixture-of-Experts Vision-Language-Action Model for Autonomous Driving
---

# SAMoE-VLA: A Scene Adaptive Mixture-of-Experts Vision-Language-Action Model for Autonomous Driving
**arXiv**：[2603.08113v1](https://arxiv.org/abs/2603.08113) · [PDF](https://arxiv.org/pdf/2603.08113.pdf)  
**作者**：Zihan You, Hongwei Liu, Chenxu Dang, Zhe Wang, Sining Ang, Aoqi Wang, Yan Wang  

**一句话要点**：提出SAMoE-VLA，基于场景自适应专家混合机制解决自动驾驶中VLA模型性能不稳定问题。

**关键词**：自动驾驶, 视觉-语言-动作模型, 专家混合机制, 场景自适应, 鸟瞰图特征, 因果注意力机制

## 3 点简述
- 核心问题：现有令牌级MoE机制在VLA模型中导致自动驾驶性能不稳定和安全下降。
- 方法要点：从鸟瞰图特征生成MoE路由信号，实现场景自适应专家选择与融合。
- 实验或效果：在nuScenes和LangAuto基准上实现最先进性能，参数更少。

## 摘要（原文）

> Recent advances in Vision-Language-Action (VLA) models have shown promising capabilities in autonomous driving by leveraging the understanding and reasoning strengths of Large Language Models(LLMs).However, our empirical analysis reveals that directly applying existing token-level MoE mechanisms--which are inherited from LLM architectures--to VLA models results in unstable performance and safety degradation in autonomous driving, highlighting a misalignment between token-based expert specialization and scene-level decision-making.To address this, we propose SAMoE-VLA, a scene-adaptive Vision-Language-Action framework that conditions expert selection on structured scene representations instead of token embeddings. Our key idea is to derive the MoE routing signal from bird's-eye-view (BEV) features that encapsulates traffic scene context, enabling scenario-dependent expert weighting and merging tailored to distinct driving conditions. Furthermore, to support temporally consistent reasoning across world-knowledge, perception, language, and action, we introduce a Conditional Cross-Modal Causal Attention mechanism that integrates world state, linguistic intent, and action history into a unified causal reasoning process. Extensive experiments on the nuScenes open loop planning dataset and LangAuto closed-loop benchmark demonstrate that SAMoE-VLA achieves state-of-the-art performance, outperforming prior VLA-based and world-model-based approaches with fewer parameters.Our code will be released soon.

