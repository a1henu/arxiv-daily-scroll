---
layout: default
title: Explainable Deepfake Detection with RL Enhanced Self-Blended Images
---

# Explainable Deepfake Detection with RL Enhanced Self-Blended Images
**arXiv**：[2601.15624v1](https://arxiv.org/abs/2601.15624) · [PDF](https://arxiv.org/pdf/2601.15624.pdf)  
**作者**：Ning Jiang, Dingheng Zeng, Yanhong Liu, Haiyang Yi, Shijie Yu, Minghe Weng, Haifeng Shen, Ying Li  

**一句话要点**：提出基于自混合图像与强化学习的可解释深度伪造检测框架，以降低标注成本并提升性能。

**关键词**：深度伪造检测, 可解释人工智能, 强化学习, 自混合图像, 跨域泛化, 多模态大语言模型

## 3 点简述
- 核心问题：现有深度伪造检测方法缺乏可解释输出，且高质量标注数据稀缺，阻碍多模态大语言模型应用。
- 方法要点：设计自动化思维链数据生成框架，结合强化学习优化检测模型，增强跨域泛化能力。
- 实验或效果：在多个跨数据集基准测试中达到与最先进方法竞争的性能，验证了数据生成和奖励机制的有效性。

## 摘要（原文）

> Most prior deepfake detection methods lack explainable outputs. With the growing interest in multimodal large language models (MLLMs), researchers have started exploring their use in interpretable deepfake detection. However, a major obstacle in applying MLLMs to this task is the scarcity of high-quality datasets with detailed forgery attribution annotations, as textual annotation is both costly and challenging - particularly for high-fidelity forged images or videos. Moreover, multiple studies have shown that reinforcement learning (RL) can substantially enhance performance in visual tasks, especially in improving cross-domain generalization. To facilitate the adoption of mainstream MLLM frameworks in deepfake detection with reduced annotation cost, and to investigate the potential of RL in this context, we propose an automated Chain-of-Thought (CoT) data generation framework based on Self-Blended Images, along with an RL-enhanced deepfake detection framework. Extensive experiments validate the effectiveness of our CoT data construction pipeline, tailored reward mechanism, and feedback-driven synthetic data generation approach. Our method achieves performance competitive with state-of-the-art (SOTA) approaches across multiple cross-dataset benchmarks. Implementation details are available at https://github.com/deon1219/rlsbi.

