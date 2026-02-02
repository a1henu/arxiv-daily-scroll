---
layout: default
title: Head-Aware Visual Cropping: Enhancing Fine-Grained VQA with Attention-Guided Subimage
---

# Head-Aware Visual Cropping: Enhancing Fine-Grained VQA with Attention-Guided Subimage
**arXiv**：[2601.22483v1](https://arxiv.org/abs/2601.22483) · [PDF](https://arxiv.org/pdf/2601.22483.pdf)  
**作者**：Junfei Xie, Peng Pan, Xulong Zhang  

**一句话要点**：提出Head-Aware Visual Cropping方法，通过注意力头筛选增强多模态大语言模型在细粒度视觉问答中的视觉定位能力。

**关键词**：细粒度视觉问答, 注意力头筛选, 视觉裁剪, 多模态大语言模型, 视觉定位增强

## 3 点简述
- 核心问题：多模态大语言模型在细粒度视觉问答中因低分辨率输入和噪声注意力聚合导致视觉定位能力受限。
- 方法要点：基于OCR诊断任务筛选注意力头，结合空间熵和梯度敏感度生成视觉裁剪指导图，引导裁剪任务相关子图像。
- 实验或效果：在多个细粒度VQA基准测试中优于现有裁剪策略，实现更精确的定位和更强的视觉基础。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) show strong performance in Visual Question Answering (VQA) but remain limited in fine-grained reasoning due to low-resolution inputs and noisy attention aggregation. We propose \textbf{Head Aware Visual Cropping (HAVC)}, a training-free method that improves visual grounding by leveraging a selectively refined subset of attention heads. HAVC first filters heads through an OCR-based diagnostic task, ensuring that only those with genuine grounding ability are retained. At inference, these heads are further refined using spatial entropy for stronger spatial concentration and gradient sensitivity for predictive contribution. The fused signals produce a reliable Visual Cropping Guidance Map, which highlights the most task-relevant region and guides the cropping of a subimage subsequently provided to the MLLM together with the image-question pair. Extensive experiments on multiple fine-grained VQA benchmarks demonstrate that HAVC consistently outperforms state-of-the-art cropping strategies, achieving more precise localization, stronger visual grounding, providing a simple yet effective strategy for enhancing precision in MLLMs.

