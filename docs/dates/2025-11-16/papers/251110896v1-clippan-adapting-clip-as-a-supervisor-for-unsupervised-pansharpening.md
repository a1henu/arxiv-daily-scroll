---
layout: default
title: CLIPPan: Adapting CLIP as A Supervisor for Unsupervised Pansharpening
---

# CLIPPan: Adapting CLIP as A Supervisor for Unsupervised Pansharpening
**arXiv**：[2511.10896v1](https://arxiv.org/abs/2511.10896) · [PDF](https://arxiv.org/pdf/2511.10896.pdf)  
**作者**：Lihua Jian, Jiabo Liu, Shaowu Wu, Lihui Chen  

**一句话要点**：提出CLIPPan框架，利用CLIP作为监督器解决无监督全分辨率全色锐化问题

**关键词**：无监督全色锐化, CLIP适应, 语义语言约束, 全分辨率训练, 图像融合

## 3 点简述
- 核心问题：监督全色锐化方法因模拟低分辨率训练数据与真实全分辨率场景差异而面临域适应挑战
- 方法要点：通过轻量微调CLIP适应全色锐化任务，并设计语义语言约束损失以语言为监督信号
- 实验或效果：在真实数据集上提升光谱和空间保真度，为无监督全分辨率全色锐化设定新基准

## 摘要（原文）

> Despite remarkable advancements in supervised pansharpening neural networks, these methods face domain adaptation challenges of resolution due to the intrinsic disparity between simulated reduced-resolution training data and real-world full-resolution scenarios.To bridge this gap, we propose an unsupervised pansharpening framework, CLIPPan, that enables model training at full resolution directly by taking CLIP, a visual-language model, as a supervisor. However, directly applying CLIP to supervise pansharpening remains challenging due to its inherent bias toward natural images and limited understanding of pansharpening tasks. Therefore, we first introduce a lightweight fine-tuning pipeline that adapts CLIP to recognize low-resolution multispectral, panchromatic, and high-resolution multispectral images, as well as to understand the pansharpening process. Then, building on the adapted CLIP, we formulate a novel \textit{loss integrating semantic language constraints}, which aligns image-level fusion transitions with protocol-aligned textual prompts (e.g., Wald's or Khan's descriptions), thus enabling CLIPPan to use language as a powerful supervisory signal and guide fusion learning without ground truth. Extensive experiments demonstrate that CLIPPan consistently improves spectral and spatial fidelity across various pansharpening backbones on real-world datasets, setting a new state of the art for unsupervised full-resolution pansharpening.

