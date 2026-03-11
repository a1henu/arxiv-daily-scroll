---
layout: default
title: Logics-Parsing-Omni Technical Report
---

# Logics-Parsing-Omni Technical Report
**arXiv**：[2603.09677v1](https://arxiv.org/abs/2603.09677) · [PDF](https://arxiv.org/pdf/2603.09677.pdf)  
**作者**：Xin An, Jingyi Cai, Xiangyang Chen, Huayao Liu, Peiting Liu, Peng Wang, Bei Yang, Xiuwen Zhu, Yongfan Chen, Baoyu Hou, Shuzhao Li, Weidong Ren, Fan Yang, Jiangtao Zhang, Xiaoxiao Xu, Lin Qu  

**一句话要点**：提出Omni Parsing框架以解决多模态解析中任务碎片化和数据异构性问题

**关键词**：多模态解析, 统一分类法, 渐进式解析, 证据锚定机制, 结构化知识转换, OmniParsingBench

## 3 点简述
- 核心问题：多模态解析面临任务定义碎片化和非结构化数据异构性挑战
- 方法要点：建立统一分类法，采用渐进式解析范式，集成整体检测、细粒度识别和多级解释三个层次
- 实验或效果：构建标准化数据集和Logics-Parsing-Omni模型，实验显示细粒度感知与高层认知协同提升模型可靠性

## 摘要（原文）

> Addressing the challenges of fragmented task definitions and the heterogeneity of unstructured data in multimodal parsing, this paper proposes the Omni Parsing framework. This framework establishes a Unified Taxonomy covering documents, images, and audio-visual streams, introducing a progressive parsing paradigm that bridges perception and cognition. Specifically, the framework integrates three hierarchical levels: 1) Holistic Detection, which achieves precise spatial-temporal grounding of objects or events to establish a geometric baseline for perception; 2) Fine-grained Recognition, which performs symbolization (e.g., OCR/ASR) and attribute extraction on localized objects to complete structured entity parsing; and 3) Multi-level Interpreting, which constructs a reasoning chain from local semantics to global logic. A pivotal advantage of this framework is its evidence anchoring mechanism, which enforces a strict alignment between high-level semantic descriptions and low-level facts. This enables ``evidence-based'' logical induction, transforming unstructured signals into standardized knowledge that is locatable, enumerable, and traceable. Building on this foundation, we constructed a standardized dataset and released the Logics-Parsing-Omni model, which successfully converts complex audio-visual signals into machine-readable structured knowledge. Experiments demonstrate that fine-grained perception and high-level cognition are synergistic, effectively enhancing model reliability. Furthermore, to quantitatively evaluate these capabilities, we introduce OmniParsingBench. Code, models and the benchmark are released at https://github.com/alibaba/Logics-Parsing/tree/master/Logics-Parsing-Omni.

