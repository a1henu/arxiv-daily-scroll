---
layout: default
title: Towards Universal Video MLLMs with Attribute-Structured and Quality-Verified Instructions
---

# Towards Universal Video MLLMs with Attribute-Structured and Quality-Verified Instructions
**arXiv**：[2602.13013v1](https://arxiv.org/abs/2602.13013) · [PDF](https://arxiv.org/pdf/2602.13013.pdf)  
**作者**：Yunheng Li, Hengrui Zhang, Meng-Hao Guo, Wenzhao Gao, Shaoyong Jia, Shaohui Jiao, Qibin Hou, Ming-Ming Cheng  

**一句话要点**：提出ASID-1M数据集与ASID-Captioner模型，以结构化指令提升通用视频理解性能。

**关键词**：视频多模态大语言模型, 结构化指令标注, 细粒度视频理解, 自动数据验证, 监督微调, 通用视频理解

## 3 点简述
- 现有视频指令数据描述粗糙，缺乏细粒度组织和可靠标注，限制模型性能。
- 引入ASID-1M结构化指令数据集和ASID-Verify验证流程，确保语义和时间一致性。
- ASID-Captioner在多个基准测试中表现优异，减少幻觉并提升指令遵循能力。

## 摘要（原文）

> Universal video understanding requires modeling fine-grained visual and audio information over time in diverse real-world scenarios. However, the performance of existing models is primarily constrained by video-instruction data that represents complex audiovisual content as single, incomplete descriptions, lacking fine-grained organization and reliable annotation. To address this, we introduce: (i) ASID-1M, an open-source collection of one million structured, fine-grained audiovisual instruction annotations with single- and multi-attribute supervision; (ii) ASID-Verify, a scalable data curation pipeline for annotation, with automatic verification and refinement that enforces semantic and temporal consistency between descriptions and the corresponding audiovisual content; and (iii) ASID-Captioner, a video understanding model trained via Supervised Fine-Tuning (SFT) on the ASID-1M. Experiments across seven benchmarks covering audiovisual captioning, attribute-wise captioning, caption-based QA, and caption-based temporal grounding show that ASID-Captioner improves fine-grained caption quality while reducing hallucinations and improving instruction following. It achieves state-of-the-art performance among open-source models and is competitive with Gemini-3-Pro.

