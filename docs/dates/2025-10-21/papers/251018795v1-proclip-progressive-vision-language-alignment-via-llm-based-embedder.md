---
layout: default
title: ProCLIP: Progressive Vision-Language Alignment via LLM-based Embedder
---

# ProCLIP: Progressive Vision-Language Alignment via LLM-based Embedder
**arXiv**：[2510.18795v1](https://arxiv.org/abs/2510.18795) · [PDF](https://arxiv.org/pdf/2510.18795.pdf)  
**作者**：Xiaoxing Hu, Kaicheng Yang, Ziyong Feng, Qi Ming, Zonghao Guo, Xiang An, Ziyong Feng, Junchi Yan, Xue Yang  

**一句话要点**：提出ProCLIP框架以解决LLM嵌入器与CLIP图像编码器对齐问题

**关键词**：视觉语言对齐, LLM嵌入器, 课程学习, 知识蒸馏, 对比学习, 多模态理解

## 3 点简述
- 核心问题：CLIP文本编码器处理长文本和多语言能力有限，直接对齐LLM嵌入器会破坏CLIP预训练知识。
- 方法要点：采用课程学习，先蒸馏CLIP文本编码器知识，再通过对比调优和自蒸馏正则化进行渐进对齐。
- 实验或效果：未知，但代码已开源，可能提升长文本和多语言视觉语言任务性能。

## 摘要（原文）

> The original CLIP text encoder is limited by a maximum input length of 77
> tokens, which hampers its ability to effectively process long texts and perform
> fine-grained semantic understanding. In addition, the CLIP text encoder lacks
> support for multilingual inputs. All these limitations significantly restrict
> its applicability across a broader range of tasks. Recent studies have
> attempted to replace the CLIP text encoder with an LLM-based embedder to
> enhance its ability in processing long texts, multilingual understanding, and
> fine-grained semantic comprehension. However, because the representation spaces
> of LLMs and the vision-language space of CLIP are pretrained independently
> without alignment priors, direct alignment using contrastive learning can
> disrupt the intrinsic vision-language alignment in the CLIP image encoder,
> leading to an underutilization of the knowledge acquired during pre-training.
> To address this challenge, we propose ProCLIP, a curriculum learning-based
> progressive vision-language alignment framework to effectively align the CLIP
> image encoder with an LLM-based embedder. Specifically, ProCLIP first distills
> knowledge from CLIP's text encoder into the LLM-based embedder to leverage
> CLIP's rich pretrained knowledge while establishing initial alignment between
> the LLM embedder and CLIP image encoder. Subsequently, ProCLIP further aligns
> the CLIP image encoder with the LLM-based embedder through image-text
> contrastive tuning, employing self-distillation regularization to avoid
> overfitting. To achieve a more effective alignment, instance semantic alignment
> loss and embedding structure alignment loss are employed during representation
> inheritance and contrastive tuning. The Code is available at
> https://github.com/VisionXLab/ProCLIP

