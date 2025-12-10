---
layout: default
title: VisKnow: Constructing Visual Knowledge Base for Object Understanding
---

# VisKnow: Constructing Visual Knowledge Base for Object Understanding
**arXiv**：[2512.08221v1](https://arxiv.org/abs/2512.08221) · [PDF](https://arxiv.org/pdf/2512.08221.pdf)  
**作者**：Ziwei Yao, Qiyang Wan, Ruiping Wang, Xilin Chen  

**一句话要点**：提出VisKnow框架以构建视觉知识库，支持深度物体理解任务。

**关键词**：视觉知识库, 物体理解, 多模态学习, 知识图谱, 零样本识别, 细粒度视觉问答

## 3 点简述
- 核心问题：现有多模态数据缺乏系统组织，难以实现全面的物体理解。
- 方法要点：结合专家设计和大规模模型，从文本和图像中提取物体级知识并构建图结构。
- 实验或效果：构建AnimalKB知识库，提升零样本识别和细粒度VQA等任务性能。

## 摘要（原文）

> Understanding objects is fundamental to computer vision. Beyond object recognition that provides only a category label as typical output, in-depth object understanding represents a comprehensive perception of an object category, involving its components, appearance characteristics, inter-category relationships, contextual background knowledge, etc. Developing such capability requires sufficient multi-modal data, including visual annotations such as parts, attributes, and co-occurrences for specific tasks, as well as textual knowledge to support high-level tasks like reasoning and question answering. However, these data are generally task-oriented and not systematically organized enough to achieve the expected understanding of object categories. In response, we propose the Visual Knowledge Base that structures multi-modal object knowledge as graphs, and present a construction framework named VisKnow that extracts multi-modal, object-level knowledge for object understanding. This framework integrates enriched aligned text and image-source knowledge with region annotations at both object and part levels through a combination of expert design and large-scale model application. As a specific case study, we construct AnimalKB, a structured animal knowledge base covering 406 animal categories, which contains 22K textual knowledge triplets extracted from encyclopedic documents, 420K images, and corresponding region annotations. A series of experiments showcase how AnimalKB enhances object-level visual tasks such as zero-shot recognition and fine-grained VQA, and serves as challenging benchmarks for knowledge graph completion and part segmentation. Our findings highlight the potential of automatically constructing visual knowledge bases to advance visual understanding and its practical applications. The project page is available at https://vipl-vsu.github.io/VisKnow.

