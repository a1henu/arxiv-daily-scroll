---
layout: default
title: VisionPangu: A Compact and Fine-Grained Multimodal Assistant with 1.7B Parameters
---

# VisionPangu: A Compact and Fine-Grained Multimodal Assistant with 1.7B Parameters
**arXiv**：[2603.04957v1](https://arxiv.org/abs/2603.04957) · [PDF](https://arxiv.org/pdf/2603.04957.pdf)  
**作者**：Jiaxin Fan, Wenpo Song  

**一句话要点**：提出VisionPangu，一个1.7B参数的多模态模型，通过高效对齐和高质量监督改进详细图像描述生成。

**关键词**：多模态模型, 图像描述生成, 参数高效, 指令调优, 紧凑架构

## 3 点简述
- 现有大型多模态模型依赖大规模架构和粗粒度监督，限制了生成详细图像描述的能力。
- 结合InternVL视觉编码器和OpenPangu-Embedded语言主干，通过轻量MLP投影器和指令调优实现高效多模态对齐。
- 实验表明，该紧凑模型能产生更具结构和细节的描述，性能具有竞争力。

## 摘要（原文）

> Large Multimodal Models (LMMs) have achieved strong performance in vision-language understanding, yet many existing approaches rely on large-scale architectures and coarse supervision, which limits their ability to generate detailed image captions. In this work, we present VisionPangu, a compact 1.7B-parameter multimodal model designed to improve detailed image captioning through efficient multimodal alignment and high-quality supervision. Our model combines an InternVL-derived vision encoder with the OpenPangu-Embedded language backbone via a lightweight MLP projector and adopts an instruction-tuning pipeline inspired by LLaVA. By incorporating dense human-authored descriptions from the DOCCI dataset, VisionPangu improves semantic coherence and descriptive richness without relying on aggressive model scaling. Experimental results demonstrate that compact multimodal models can achieve competitive performance while producing more structured and detailed captions. The code and model weights will be publicly available at https://www.modelscope.cn/models/asdfgh007/visionpangu.

