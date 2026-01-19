---
layout: default
title: SAMannot: A Memory-Efficient, Local, Open-source Framework for Interactive Video Instance Segmentation based on SAM2
---

# SAMannot: A Memory-Efficient, Local, Open-source Framework for Interactive Video Instance Segmentation based on SAM2
**arXiv**：[2601.11301v1](https://arxiv.org/abs/2601.11301) · [PDF](https://arxiv.org/pdf/2601.11301.pdf)  
**作者**：Gergely Dinya, András Gelencsér, Krisztina Kupán, Clemens Küpper, Kristóf Karacs, Anna Gelencsér-Horváth  

**一句话要点**：提出SAMannot框架，基于SAM2实现本地交互式视频实例分割，解决手动标注耗时和隐私问题。

**关键词**：视频实例分割, 交互式标注, 本地框架, SAM2集成, 隐私保护, 自动提示

## 3 点简述
- 核心问题：视频实例分割依赖手动标注或云服务，存在效率低和隐私风险。
- 方法要点：集成SAM2，优化资源使用，支持身份管理和自动提示，提升交互效率。
- 实验或效果：在动物行为跟踪和LVOS/DAVIS数据集验证，提供可扩展、私有且经济的替代方案。

## 摘要（原文）

> Current research workflows for precise video segmentation are often forced into a compromise between labor-intensive manual curation, costly commercial platforms, and/or privacy-compromising cloud-based services. The demand for high-fidelity video instance segmentation in research is often hindered by the bottleneck of manual annotation and the privacy concerns of cloud-based tools. We present SAMannot, an open-source, local framework that integrates the Segment Anything Model 2 (SAM2) into a human-in-the-loop workflow. To address the high resource requirements of foundation models, we modified the SAM2 dependency and implemented a processing layer that minimizes computational overhead and maximizes throughput, ensuring a highly responsive user interface. Key features include persistent instance identity management, an automated ``lock-and-refine'' workflow with barrier frames, and a mask-skeletonization-based auto-prompting mechanism. SAMannot facilitates the generation of research-ready datasets in YOLO and PNG formats alongside structured interaction logs. Verified through animal behavior tracking use-cases and subsets of the LVOS and DAVIS benchmark datasets, the tool provides a scalable, private, and cost-effective alternative to commercial platforms for complex video annotation tasks.

