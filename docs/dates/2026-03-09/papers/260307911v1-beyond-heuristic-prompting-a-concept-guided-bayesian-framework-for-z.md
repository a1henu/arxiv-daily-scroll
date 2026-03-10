---
layout: default
title: Beyond Heuristic Prompting: A Concept-Guided Bayesian Framework for Zero-Shot Image Recognition
---

# Beyond Heuristic Prompting: A Concept-Guided Bayesian Framework for Zero-Shot Image Recognition
**arXiv**：[2603.07911v1](https://arxiv.org/abs/2603.07911) · [PDF](https://arxiv.org/pdf/2603.07911.pdf)  
**作者**：Hui Liu, Kecheng Chen, Jialiang Wang, Xianming Liu, Wenya Wang, Haoliang Li  

**一句话要点**：提出概念引导的贝叶斯框架以提升零样本图像识别的性能

**关键词**：零样本图像识别, 贝叶斯框架, 概念引导, 提示工程, 多阶段合成, 软修剪似然

## 3 点简述
- 核心问题：现有方法依赖启发式提示，缺乏适应性且易受异常提示影响
- 方法要点：基于贝叶斯视角，将概念作为隐变量，通过多阶段合成和软修剪似然优化预测
- 实验或效果：在零样本图像分类中一致超越先进方法，提供鲁棒性保证和风险界限

## 摘要（原文）

> Vision-Language Models (VLMs), such as CLIP, have significantly advanced zero-shot image recognition. However, their performance remains limited by suboptimal prompt engineering and poor adaptability to target classes. While recent methods attempt to improve prompts through diverse class descriptions, they often rely on heuristic designs, lack versatility, and are vulnerable to outlier prompts. This paper enhances prompt by incorporating class-specific concepts. By treating concepts as latent variables, we rethink zero-shot image classification from a Bayesian perspective, casting prediction as marginalization over the concept space, where each concept is weighted by a prior and a test-image conditioned likelihood. This formulation underscores the importance of both a well-structured concept proposal distribution and the refinement of concept priors. To construct an expressive and efficient proposal distribution, we introduce a multi-stage concept synthesis pipeline driven by LLMs to generate discriminative and compositional concepts, followed by a Determinantal Point Process to enforce diversity. To mitigate the influence of outlier concepts, we propose a training-free, adaptive soft-trim likelihood, which attenuates their impact in a single forward pass. We further provide robustness guarantees and derive multi-class excess risk bounds for our framework. Extensive experiments demonstrate that our method consistently outperforms state-of-the-art approaches, validating its effectiveness in zero-shot image classification. Our code is available at https://github.com/less-and-less-bugs/CGBC.

