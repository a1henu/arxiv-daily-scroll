---
layout: default
title: Mixture of Lookup Key-Value Experts
---

# Mixture of Lookup Key-Value Experts
**arXiv**：[2512.09723v1](https://arxiv.org/abs/2512.09723) · [PDF](https://arxiv.org/pdf/2512.09723.pdf)  
**作者**：Zongcheng Wang  

**一句话要点**：提出MoLKV模型以解决MoLE上下文无关专家选择限制，提升资源受限设备上LLM性能。

**关键词**：专家混合模型, 上下文感知机制, 键值对专家, 资源受限设备, LLM推理优化

## 3 点简述
- MoLE基于输入ID选择专家，上下文无关，可能限制模型性能。
- MoLKV将专家构建为键值对，通过输入查询与缓存键值交互实现上下文感知输出。
- 小规模评估显示MoLKV显著降低验证损失，优于MoLE。

## 摘要（原文）

> Recent research has developed several LLM architectures suitable for inference on end-user devices, such as the Mixture of Lookup Experts (MoLE)~\parencite{jie_mixture_2025}. A key feature of MoLE is that each token id is associated with a dedicated group of experts. For a given input, only the experts corresponding to the input token id will be activated. Since the communication overhead of loading this small number of activated experts into RAM during inference is negligible, expert parameters can be offloaded to storage, making MoLE suitable for resource-constrained devices. However, MoLE's context-independent expert selection mechanism, based solely on input ids, may limit model performance. To address this, we propose the \textbf{M}ixture \textbf{o}f \textbf{L}ookup \textbf{K}ey-\textbf{V}alue Experts (\textbf{MoLKV}) model. In MoLKV, each expert is structured as a key-value pair. For a given input, the input-derived query interacts with the cached key-value experts from the current sequence, generating a context-aware expert output. This context-aware mechanism alleviates the limitation of MoLE, and experimental results demonstrate that MoLKV achieves significantly lower validation loss in small-scale evaluations.

