---
layout: default
title: AIForge-Doc: A Benchmark for Detecting AI-Forged Tampering in Financial and Form Documents
---

# AIForge-Doc: A Benchmark for Detecting AI-Forged Tampering in Financial and Form Documents
**arXiv**：[2602.20569v1](https://arxiv.org/abs/2602.20569) · [PDF](https://arxiv.org/pdf/2602.20569.pdf)  
**作者**：Jiaqi Wu, Yuchen Zhou, Muduo Xu, Zisheng Liang, Simiao Ren, Jiayu Xue, Meige Yang, Siying Chen, Jingheng Huan  

**一句话要点**：提出AIForge-Doc基准，专门检测金融表单文档中基于扩散模型的AI伪造篡改

**关键词**：文档伪造检测, 扩散模型, 基准数据集, 金融文档, 像素级标注, AI伪造

## 3 点简述
- 现有文档伪造数据集依赖传统编辑工具，无法应对AI伪造威胁
- 使用Gemini和Ideogram API系统伪造数字字段，构建多语言数据集
- 测试显示现有检测方法性能大幅下降，AI伪造成为未解决挑战

## 摘要（原文）

> We present AIForge-Doc, the first dedicated benchmark targeting exclusively diffusion-model-based inpainting in financial and form documents with pixel-level annotation. Existing document forgery datasets rely on traditional digital editing tools (e.g., Adobe Photoshop, GIMP), creating a critical gap: state-of-the-art detectors are blind to the rapidly growing threat of AI-forged document fraud. AIForge-Doc addresses this gap by systematically forging numeric fields in real-world receipt and form images using two AI inpainting APIs -- Gemini 2.5 Flash Image and Ideogram v2 Edit -- yielding 4,061 forged images from four public document datasets (CORD, WildReceipt, SROIE, XFUND) across nine languages, annotated with pixel-precise tampered-region masks in DocTamper-compatible format. We benchmark three representative detectors -- TruFor, DocTamper, and a zero-shot GPT-4o judge -- and find that all existing methods degrade substantially: TruFor achieves AUC=0.751 (zero-shot, out-of-distribution) vs. AUC=0.96 on NIST16; DocTamper achieves AUC=0.563 vs. AUC=0.98 in-distribution, with pixel-level IoU=0.020; GPT-4o achieves only 0.509 -- essentially at chance -- confirming that AI-forged values are indistinguishable to automated detectors and VLMs. These results demonstrate that AIForge-Doc represents a qualitatively new and unsolved challenge for document forensics.

