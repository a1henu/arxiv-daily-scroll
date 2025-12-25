---
layout: default
title: Benchmarking and Enhancing VLM for Compressed Image Understanding
---

# Benchmarking and Enhancing VLM for Compressed Image Understanding
**arXiv**：[2512.20901v1](https://arxiv.org/abs/2512.20901) · [PDF](https://arxiv.org/pdf/2512.20901.pdf)  
**作者**：Zifu Zhang, Tongda Xu, Siqi Li, Shengxi Li, Yue Zhang, Mai Xu, Yan Wang  

**一句话要点**：提出通用适配器以增强视觉语言模型对压缩图像的理解能力

**关键词**：视觉语言模型, 图像压缩, 基准测试, 泛化能力, 模型适配器

## 3 点简述
- 首次建立评估视觉语言模型处理压缩图像的基准，涵盖多种编解码器和任务
- 分析性能差距源于压缩信息损失和模型泛化失败，后者可被缓解
- 设计通用适配器，提升模型在不同编解码器和比特率下的性能10%-30%

## 摘要（原文）

> With the rapid development of Vision-Language Models (VLMs) and the growing demand for their applications, efficient compression of the image inputs has become increasingly important. Existing VLMs predominantly digest and understand high-bitrate compressed images, while their ability to interpret low-bitrate compressed images has yet to be explored by far. In this paper, we introduce the first comprehensive benchmark to evaluate the ability of VLM against compressed images, varying existing widely used image codecs and diverse set of tasks, encompassing over one million compressed images in our benchmark. Next, we analyse the source of performance gap, by categorising the gap from a) the information loss during compression and b) generalisation failure of VLM. We visualize these gaps with concrete examples and identify that for compressed images, only the generalization gap can be mitigated. Finally, we propose a universal VLM adaptor to enhance model performance on images compressed by existing codecs. Consequently, we demonstrate that a single adaptor can improve VLM performance across images with varying codecs and bitrates by 10%-30%. We believe that our benchmark and enhancement method provide valuable insights and contribute toward bridging the gap between VLMs and compressed images.

