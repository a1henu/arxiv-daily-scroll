---
layout: default
title: Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception
---

# Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception
**arXiv**：[2602.11858v1](https://arxiv.org/abs/2602.11858) · [PDF](https://arxiv.org/pdf/2602.11858.pdf)  
**作者**：Lai Wei, Liangbo He, Jun Lan, Lingzhong Dong, Yutong Cai, Siyuan Li, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang, Weiran Huang  

**一句话要点**：提出区域到图像蒸馏方法，将推理时缩放转化为训练时操作，提升多模态大语言模型的细粒度感知能力。

**关键词**：细粒度感知, 区域到图像蒸馏, 多模态大语言模型, 视觉问答, 训练时优化, 推理加速

## 3 点简述
- 核心问题：多模态大语言模型在细粒度感知中，关键证据小且易被全局上下文淹没，现有方法推理延迟高。
- 方法要点：通过微裁剪区域生成高质量VQA数据，蒸馏回完整图像，使模型在单次前向传播中内化缩放优势。
- 实验或效果：在ZoomBench等基准上取得领先性能，同时提升视觉推理和GUI代理等一般多模态认知能力。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) excel at broad visual understanding but still struggle with fine-grained perception, where decisive evidence is small and easily overwhelmed by global context. Recent "Thinking-with-Images" methods alleviate this by iteratively zooming in and out regions of interest during inference, but incur high latency due to repeated tool calls and visual re-encoding. To address this, we propose Region-to-Image Distillation, which transforms zooming from an inference-time tool into a training-time primitive, thereby internalizing the benefits of agentic zooming into a single forward pass of an MLLM. In particular, we first zoom in to micro-cropped regions to let strong teacher models generate high-quality VQA data, and then distill this region-grounded supervision back to the full image. After training on such data, the smaller student model improves "single-glance" fine-grained perception without tool use. To rigorously evaluate this capability, we further present ZoomBench, a hybrid-annotated benchmark of 845 VQA data spanning six fine-grained perceptual dimensions, together with a dual-view protocol that quantifies the global--regional "zooming gap". Experiments show that our models achieve leading performance across multiple fine-grained perception benchmarks, and also improve general multimodal cognition on benchmarks such as visual reasoning and GUI agents. We further discuss when "Thinking-with-Images" is necessary versus when its gains can be distilled into a single forward pass. Our code is available at https://github.com/inclusionAI/Zooming-without-Zooming.

