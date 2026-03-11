---
layout: default
title: CogBlender: Towards Continuous Cognitive Intervention in Text-to-Image Generation
---

# CogBlender: Towards Continuous Cognitive Intervention in Text-to-Image Generation
**arXiv**：[2603.09286v1](https://arxiv.org/abs/2603.09286) · [PDF](https://arxiv.org/pdf/2603.09286.pdf)  
**作者**：Shengqi Dang, Jiaying Lei, Yi He, Ziqing Qian, Nan Cao  

**一句话要点**：提出CogBlender框架，通过连续多维干预实现文本到图像生成中的认知属性控制。

**关键词**：文本到图像生成, 认知属性控制, 流匹配, 连续干预, 创意设计

## 3 点简述
- 核心问题：现有文本到图像模型难以控制图像的认知属性（如情感、记忆性），无法满足心理意图。
- 方法要点：构建认知空间与语义流形映射，定义认知锚点，通过流匹配过程的速度场插值实现连续多维干预。
- 实验或效果：在效价、唤醒度、支配度和图像记忆性四个维度验证有效性，支持认知驱动的创意设计。

## 摘要（原文）

> Beyond conveying semantic information, an image can also manifest cognitive attributes that elicit specific cognitive processes from the viewer, such as memory encoding or emotional response. While modern text-to-image models excel at generating semantically coherent content, they remain limited in their ability to control such cognitive properties of images (e.g., valence, memorability), often failing to align with the specific psychological intent. To bridge this gap, we introduce CogBlender, a framework that enables continuous and multi-dimensional intervention of cognitive properties during text-to-image generation. Our approach is built upon a mapping between the Cognitive Space, representing the space of cognitive properties, and the Semantic Manifold, representing the manifold of the visual semantics. We define a set of Cognitive Anchors, serving as the boundary points for the cognitive space. Then we reformulate the velocity field within the flow-matching process by interpolating from the velocity field of different anchors. Consequently, the generative process is driven by the velocity field and dynamically steered by multi-dimensional cognitive scores, enabling precise, fine-grained, and continuous intervention. We validate the effectiveness of CogBlender across four representative cognitive dimensions: valence, arousal, dominance, and image memorability. Extensive experiments demonstrate that our method achieves effective cognitive intervention. Our work provides an effective paradigm for cognition-driven creative design.

