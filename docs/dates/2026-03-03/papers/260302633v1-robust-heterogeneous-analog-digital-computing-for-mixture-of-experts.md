---
layout: default
title: Robust Heterogeneous Analog-Digital Computing for Mixture-of-Experts Models with Theoretical Generalization Guarantees
---

# Robust Heterogeneous Analog-Digital Computing for Mixture-of-Experts Models with Theoretical Generalization Guarantees
**arXiv**：[2603.02633v1](https://arxiv.org/abs/2603.02633) · [PDF](https://arxiv.org/pdf/2603.02633.pdf)  
**作者**：Mohammed Nowaz Rabbani Chowdhury, Hsinyu Tsai, Geoffrey W. Burr, Kaoutar El Maghraoui, Liu Liu, Meng Wang  

**一句话要点**：提出免重训练的异构计算框架，以解决混合专家模型在模拟内存计算中的噪声敏感性问题。

**关键词**：混合专家模型, 模拟内存计算, 异构计算, 噪声鲁棒性, 免重训练, 语言模型

## 3 点简述
- 稀疏混合专家模型参数庞大，导致推理时内存和能效低下，模拟内存计算可减少数据移动但存在硬件非理想性。
- 通过最大神经元范数识别噪声敏感专家，将其分配至数字计算，而多数专家在模拟硬件上执行，无需重训练。
- 在DeepSeekMoE和OLMoE等大型模型上实验，验证了该方法在模拟非理想性下保持准确性的鲁棒性。

## 摘要（原文）

> Sparse Mixture-of-Experts (MoE) models enable efficient scalability by activating only a small sub-set of experts per input, yet their massive parameter counts lead to substantial memory and energy inefficiency during inference. Analog in-memory computing (AIMC) offers a promising solution by eliminating frequent data movement between memory and compute units. However, mitigating hardware nonidealities of AIMC typically requires noise-aware retraining, which is infeasible for large MoE models. In this paper, we propose a retraining-free heterogeneous computation framework in which noise-sensitive experts, which are provably identifiable by their maximum neuron norm, are computed digitally while the majority of the experts are executed on AIMC hardware. We further assign densely activated modules, such as attention layers, to digital computation due to their high noise sensitivity despite comprising a small fraction of parameters. Extensive experiments on large MoE language models, including DeepSeekMoE and OLMoE, across multiple benchmark tasks validate the robustness of our approach in maintaining accuracy under analog nonidealities.

