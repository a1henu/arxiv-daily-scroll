---
layout: default
title: LLM4Fluid: Large Language Models as Generalizable Neural Solvers for Fluid Dynamics
---

# LLM4Fluid: Large Language Models as Generalizable Neural Solvers for Fluid Dynamics
**arXiv**：[2601.21681v1](https://arxiv.org/abs/2601.21681) · [PDF](https://arxiv.org/pdf/2601.21681.pdf)  
**作者**：Qisong Xiao, Xinhai Chen, Qinglin Wang, Xiaowei Guo, Binglin Wang, Weifeng Chen, Zhichao Wang, Yunfei Liu, Rui Xia, Hang Zou, Gencheng Liu, Shuai Li, Jie Liu  

**一句话要点**：提出LLM4Fluid框架，利用大语言模型作为通用神经求解器解决流体动力学泛化问题。

**关键词**：流体动力学建模, 大语言模型应用, 时空预测, 降阶建模, 模态对齐, 零样本学习

## 3 点简述
- 现有深度学习方法在流体动力学建模中泛化能力有限，需针对新场景重新训练。
- 框架通过降阶建模压缩流场，并利用预训练LLM进行时序预测，结合模态对齐策略提升准确性。
- 实验表明LLM4Fluid无需重新训练，在多种流场景中实现高精度，具备零样本和上下文学习能力。

## 摘要（原文）

> Deep learning has emerged as a promising paradigm for spatio-temporal modeling of fluid dynamics. However, existing approaches often suffer from limited generalization to unseen flow conditions and typically require retraining when applied to new scenarios. In this paper, we present LLM4Fluid, a spatio-temporal prediction framework that leverages Large Language Models (LLMs) as generalizable neural solvers for fluid dynamics. The framework first compresses high-dimensional flow fields into a compact latent space via reduced-order modeling enhanced with a physics-informed disentanglement mechanism, effectively mitigating spatial feature entanglement while preserving essential flow structures. A pretrained LLM then serves as a temporal processor, autoregressively predicting the dynamics of physical sequences with time series prompts. To bridge the modality gap between prompts and physical sequences, which can otherwise degrade prediction accuracy, we propose a dedicated modality alignment strategy that resolves representational mismatch and stabilizes long-term prediction. Extensive experiments across diverse flow scenarios demonstrate that LLM4Fluid functions as a robust and generalizable neural solver without retraining, achieving state-of-the-art accuracy while exhibiting powerful zero-shot and in-context learning capabilities. Code and datasets are publicly available at https://github.com/qisongxiao/LLM4Fluid.

