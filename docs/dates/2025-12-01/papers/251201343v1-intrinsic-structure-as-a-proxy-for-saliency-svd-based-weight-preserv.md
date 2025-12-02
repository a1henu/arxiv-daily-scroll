---
layout: default
title: Intrinsic Structure as a Proxy for Saliency: SVD-Based Weight Preservation for Mixed-Precision Quantization in Large Language Models
---

# Intrinsic Structure as a Proxy for Saliency: SVD-Based Weight Preservation for Mixed-Precision Quantization in Large Language Models
**arXiv**：[2512.01343v1](https://arxiv.org/abs/2512.01343) · [PDF](https://arxiv.org/pdf/2512.01343.pdf)  
**作者**：Shashank Landge, Abhishek Patil, Tejas kamble, Bhushan Buddhivant, Priyanka Joshi  

**一句话要点**：提出基于SVD的结构感知权重选择方法，以解决无校准数据下大语言模型混合精度量化问题。

**关键词**：大语言模型量化, 混合精度量化, 奇异值分解, 权重选择, 数据自由方法, 结构重要性

## 3 点简述
- 核心问题：大语言模型量化中，均匀量化因关键权重（异常特征）导致性能下降，且现有方法依赖校准数据，在数据隐私或缺失场景下不适用。
- 方法要点：假设奇异值分解识别的主成分权重对模型性能至关重要，提出数据自由选择启发式，保留FP32精度主成分权重，其余权重进行激进量化。
- 实验或效果：在GLUE基准测试中，基于SVD的方法在RTE任务上达到66.06%准确率，优于AWQ和SpQR，验证结构重要性可作为权重显著性的稳健代理。

## 摘要（原文）

> As Large Language Models (LLMs) continue to scale in parameter count, deploying them on commodity hardware has become increasingly challenging. Post-Training Quantization (PTQ) addresses this by reducing the precision of model weights, typically to 4-bit or lower. However, uniform quantization often leads to significant performance degradation due to the presence of ``outlier features'' -- weights that, while few in number, are critical for maintaining model accuracy. Current state-of-the-art methods such as AWQ (Activation-aware Weight Quantization) and SpQR (Sparse Quantization Representations) rely on calibration data to identify these salient weights via activation magnitudes or Hessian sensitivity. In scenarios where data privacy is paramount or calibration data is unavailable, these methods are inapplicable.
>   In this work, we propose a data-free, structure-aware hypothesis: that the weights identified as Principal Components via Singular Value Decomposition (SVD) are intrinsically important to the model's downstream performance. We introduce a novel selection heuristic that preserves the top-$k$ weights aligned with the principal components in FP32, while aggressively quantizing the residual weights. We compare our method against activation-aware (AWQ) and second-order (SpQR) methods across GLUE benchmarks (MRPC, RTE, QNLI) using a DistilBERT backbone. Our experiments reveal that structural importance is highly correlated with functional importance. On the challenging RTE task, our SVD-based method achieves an accuracy of 66.06\%, outperforming both AWQ (65.34\%) and SpQR (65.34\%) at high protection budgets, validating that intrinsic matrix structure can serve as a robust proxy for weight saliency without the need for forward passes or calibration data.

