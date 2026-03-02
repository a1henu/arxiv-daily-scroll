---
layout: default
title: Suppressing Prior-Comparison Hallucinations in Radiology Report Generation via Semantically Decoupled Latent Steering
---

# Suppressing Prior-Comparison Hallucinations in Radiology Report Generation via Semantically Decoupled Latent Steering
**arXiv**：[2602.23676v1](https://arxiv.org/abs/2602.23676) · [PDF](https://arxiv.org/pdf/2602.23676.pdf)  
**作者**：Ao Li, Rui Liu, Mingjie Li, Sheng Liu, Lei Wang, Xiaodan Liang, Lina Yao, Xiaojun Chang, Lei Xing  

**一句话要点**：提出语义解耦潜在导向框架以抑制放射学报告生成中的先验比较幻觉

**关键词**：放射学报告生成, 先验比较幻觉, 语义解耦, 潜在导向, 推理控制, 视觉语言模型

## 3 点简述
- 核心问题：视觉语言模型在放射学报告生成中易产生无当前研究支持的先验比较幻觉。
- 方法要点：通过大语言模型语义分解和QR正交化构建语义无关干预向量，实现训练无关的推理控制。
- 实验或效果：在MIMIC-CXR上显著降低幻觉概率并提高临床标签保真度，保持临床叙述结构完整性。

## 摘要（原文）

> Automated radiology report generation using vision-language models (VLMs) is limited by the risk of prior-comparison hallucination, where the model generates historical findings unsupported by the current study. We address this challenge with a training-free, inference-time control framework termed Semantically Decoupled Latent Steering (SDLS). Unlike generic activation steering, which often suffers from semantic entanglement, our approach constructs a semantic-free intervention vector via large language model (LLM)-driven semantic decomposition followed by $QR$-based orthogonalization. This orthogonalization step is critical. It leverages geometric constraints to filter out the clinical semantics often entangled in standard principal component analysis (PCA) directions, ensuring that the steering vector targets only the ``historical comparison" axis. We validate our method on the BiomedGPT foundation model, demonstrating that it overcomes the trade-off between hallucination suppression and clinical accuracy. Extensive experiments on MIMIC-CXR, and zero-shot transfer evaluation on CheXpert Plus and IU-Xray, demonstrate the robustness of our approach. Quantitative evaluations on MIMIC-CXR show that our approach significantly reduces the probability of historical hallucinations (FilBERT score decreases from 0.2373 to 0.1889) and improves clinical label fidelity (CheXpert macro-F1 increases from 0.2242 to 0.3208). Supplementary evaluations confirm that the structural integrity of the clinical narrative is maintained.

