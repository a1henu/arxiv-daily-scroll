---
layout: default
title: ALTER: Asymmetric LoRA for Token-Entropy-Guided Unlearning of LLMs
---

# ALTER: Asymmetric LoRA for Token-Entropy-Guided Unlearning of LLMs
**arXiv**：[2603.01792v1](https://arxiv.org/abs/2603.01792) · [PDF](https://arxiv.org/pdf/2603.01792.pdf)  
**作者**：Xunlei Chen, Jinyu Guo, Yuang Li, Zhaokun Wang, Yi Gong, Jie Zou, Jiwei Wei, Wenhong Tian  

**一句话要点**：提出ALTER框架，通过非对称LoRA实现基于令牌熵引导的大语言模型遗忘，以解决知识纠缠与效率问题。

**关键词**：大语言模型遗忘, 非对称LoRA, 令牌熵引导, 知识纠缠, 参数隔离, 轻量级框架

## 3 点简述
- 核心问题：大语言模型在连续多域训练中知识纠缠，导致遗忘时边界模糊且易造成附带损伤。
- 方法要点：采用两阶段方法，先通过共享A矩阵学习高熵令牌，再通过非对称LoRA架构隔离参数并遗忘目标子域令牌。
- 实验或效果：在TOFU、WMDP和MUSE基准上实现超过95%的遗忘质量，模型效用保持率超90%，效率优异。

## 摘要（原文）

> Large language models (LLMs) have advanced to encompass extensive knowledge across diverse domains. Yet controlling what a LLMs should not know is important for ensuring alignment and thus safe use. However, effective unlearning in LLMs is difficult due to the fuzzy boundary between knowledge retention and forgetting. This challenge is exacerbated by entangled parameter spaces from continuous multi-domain training, often resulting in collateral damage, especially under aggressive unlearning strategies. Furthermore, the computational overhead required to optimize State-of-the-Art (SOTA) models with billions of parameters poses an additional barrier. In this work, we present ALTER, a lightweight unlearning framework for LLMs to address both the challenges of knowledge entanglement and unlearning efficiency. ALTER operates through two phases: (I) high entropy tokens are captured and learned via the shared A matrix in LoRA, followed by (II) an asymmetric LoRA architecture that achieves a specified forgetting objective by parameter isolation and unlearning tokens within the target subdomains. Serving as a new research direction for achieving unlearning via token-level isolation in the asymmetric framework. ALTER achieves SOTA performance on TOFU, WMDP, and MUSE benchmarks with over 95% forget quality and shows minimal side effects through preserving foundational tokens. By decoupling unlearning from LLMs' billion-scale parameters, this framework delivers excellent efficiency while preserving over 90% of model utility, exceeding baseline preservation rates of 47.8-83.6%.

