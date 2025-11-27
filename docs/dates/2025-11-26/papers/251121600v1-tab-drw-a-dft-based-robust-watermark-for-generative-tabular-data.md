---
layout: default
title: TAB-DRW: A DFT-based Robust Watermark for Generative Tabular Data
---

# TAB-DRW: A DFT-based Robust Watermark for Generative Tabular Data
**arXiv**：[2511.21600v1](https://arxiv.org/abs/2511.21600) · [PDF](https://arxiv.org/pdf/2511.21600.pdf)  
**作者**：Yizhou Zhao, Xiang Li, Peter Song, Qi Long, Weijie Su  

**一句话要点**：提出TAB-DRW以解决生成表格数据的水印嵌入与鲁棒性问题

**关键词**：表格数据水印, 离散傅里叶变换, 鲁棒水印, 生成式AI, 数据溯源

## 3 点简述
- 生成式AI产生高保真表格数据，引发数据溯源和滥用的担忧
- 在频域嵌入水印，使用DFT调整虚部，支持混合类型特征
- 实验显示高检测性和鲁棒性，保持数据保真度

## 摘要（原文）

> The rise of generative AI has enabled the production of high-fidelity synthetic tabular data across fields such as healthcare, finance, and public policy, raising growing concerns about data provenance and misuse. Watermarking offers a promising solution to address these concerns by ensuring the traceability of synthetic data, but existing methods face many limitations: they are computationally expensive due to reliance on large diffusion models, struggle with mixed discrete-continuous data, or lack robustness to post-modifications. To address them, we propose TAB-DRW, an efficient and robust post-editing watermarking scheme for generative tabular data. TAB-DRW embeds watermark signals in the frequency domain: it normalizes heterogeneous features via the Yeo-Johnson transformation and standardization, applies the discrete Fourier transform (DFT), and adjusts the imaginary parts of adaptively selected entries according to precomputed pseudorandom bits. To further enhance robustness and efficiency, we introduce a novel rank-based pseudorandom bit generation method that enables row-wise retrieval without incurring storage overhead. Experiments on five benchmark tabular datasets show that TAB-DRW achieves strong detectability and robustness against common post-processing attacks, while preserving high data fidelity and fully supporting mixed-type features.

