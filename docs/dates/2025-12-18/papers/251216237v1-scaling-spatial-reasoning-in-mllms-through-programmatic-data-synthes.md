---
layout: default
title: Scaling Spatial Reasoning in MLLMs through Programmatic Data Synthesis
---

# Scaling Spatial Reasoning in MLLMs through Programmatic Data Synthesis
**arXiv**：[2512.16237v1](https://arxiv.org/abs/2512.16237) · [PDF](https://arxiv.org/pdf/2512.16237.pdf)  
**作者**：Zhi Helu, Huang Jingjing, Xu Wang, Xu Yangbin, Zhang Wanyue, Jiang Baoyang, Deng Shirui, Zhu Liang, Li Fangfang, Zhao Tiejun, Lin Yankai, Yao Yuan  

**一句话要点**：提出SPRITE框架，通过程序化数据合成解决多模态大模型空间推理数据可扩展性与精确性难题

**关键词**：空间推理, 程序化数据合成, 多模态大模型, 模拟器验证, 指令调优

## 3 点简述
- 核心问题：现有方法在空间推理数据生成上存在模板僵化与人工标注不可扩展且不精确的困境
- 方法要点：利用大模型将空间问题编译为可执行程序，结合模拟器元信息验证，实现高质量数据合成
- 实验或效果：构建包含300k+样本的数据集，训练模型在多个空间基准测试中显著优于同等规模开源数据集

## 摘要（原文）

> Embodied intelligence, a grand challenge in artificial intelligence, is fundamentally constrained by the limited spatial understanding and reasoning capabilities of current models. Prevailing efforts to address this through enhancing Vision-Language Models (VLMs) are trapped in a dilemma: template-based datasets are scalable but structurally rigid, while manual annotation is linguistically diverse but unscalable and, critically, computationally imprecise. We introduce SPRITE, a novel framework that overcomes this dilemma by leveraging simulators and large models to programmatically synthesize scalable, diverse, and high-quality spatial reasoning data. The core innovation of SPRITE is to reframe ground-truth generation as a code-generation task. We utilize LLMs to compile complex spatial questions into executable programs, which are then verified against high-precision scene meta-information extracted from simulators. This ensures our ground truth is both computationally precise and verifiable, while the generative power of LLMs provides vast linguistic diversity. Leveraging this pipeline, we have curated a dataset encompassing 3 simulators, 11k+ scenes, and 300k+ image/video instruction-tuning pairs. We demonstrate that a VLM trained on our data achieves significant performance gains on multiple spatial benchmarks and outperforms other open-source datasets of equivalent size. Furthermore, a scalability analysis confirms our hypothesis that overcoming the low-diversity nature of traditional template methods is essential for building robust, generalizable spatial intelligence. We will make the SPRITE framework code and the full 300k+ dataset publicly available to facilitate future research in spatial intelligence.

