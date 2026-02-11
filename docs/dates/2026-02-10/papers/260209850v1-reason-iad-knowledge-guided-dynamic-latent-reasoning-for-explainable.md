---
layout: default
title: Reason-IAD: Knowledge-Guided Dynamic Latent Reasoning for Explainable Industrial Anomaly Detection
---

# Reason-IAD: Knowledge-Guided Dynamic Latent Reasoning for Explainable Industrial Anomaly Detection
**arXiv**：[2602.09850v1](https://arxiv.org/abs/2602.09850) · [PDF](https://arxiv.org/pdf/2602.09850.pdf)  
**作者**：Peng Chen, Chao Huang, Yunkang Cao, Chengliang Liu, Wenqiang Wang, Mingbo Yang, Li Shen, Wenqi Ren, Xiaochun Cao  

**一句话要点**：提出Reason-IAD框架，通过知识引导的动态潜在推理解决工业异常检测的准确性和可解释性问题。

**关键词**：工业异常检测, 多模态大语言模型, 知识引导推理, 潜在空间探索, 可解释性分析

## 3 点简述
- 核心问题：现有多模态大语言模型在工业异常检测中难以捕捉类别特定异常，影响检测精度和可解释性。
- 方法要点：结合检索增强知识模块和熵驱动潜在推理机制，动态注入关键图像补丁，实现上下文感知推理。
- 实验或效果：在实验中优于现有先进方法，代码将公开提供。

## 摘要（原文）

> Industrial anomaly detection demands precise reasoning over fine-grained defect patterns. However, existing multimodal large language models (MLLMs), pretrained on general-domain data, often struggle to capture category-specific anomalies, thereby limiting both detection accuracy and interpretability. To address these limitations, we propose Reason-IAD, a knowledge-guided dynamic latent reasoning framework for explainable industrial anomaly detection. Reason-IAD comprises two core components. First, a retrieval-augmented knowledge module incorporates category-specific textual descriptions into the model input, enabling context-aware reasoning over domain-specific defects. Second, an entropy-driven latent reasoning mechanism conducts iterative exploration within a compact latent space using optimizable latent think tokens, guided by an entropy-based reward that encourages confident and stable predictions. Furthermore, a dynamic visual injection strategy selectively incorporates the most informative image patches into the latent sequence, directing the reasoning process toward regions critical for anomaly detection. Extensive experimental results demonstrate that Reason-IAD consistently outperforms state-of-the-art methods. The code will be publicly available at https://github.com/chenpeng052/Reason-IAD.

