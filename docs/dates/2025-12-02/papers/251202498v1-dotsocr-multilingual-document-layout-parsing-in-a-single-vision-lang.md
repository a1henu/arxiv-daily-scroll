---
layout: default
title: dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model
---

# dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model
**arXiv**：[2512.02498v1](https://arxiv.org/abs/2512.02498) · [PDF](https://arxiv.org/pdf/2512.02498.pdf)  
**作者**：Yumeng Li, Guang Yang, Hao Liu, Bowen Wang, Colin Zhang  

**一句话要点**：提出dots.ocr统一视觉语言模型，以端到端方式联合学习文档布局解析核心任务，解决多阶段流程错误传播问题。

**关键词**：文档布局解析, 视觉语言模型, 端到端学习, 多语言处理, 统一框架

## 3 点简述
- 当前文档布局解析方法依赖多阶段流程，易导致错误传播且无法利用联合训练优势。
- dots.ocr首次在统一框架内联合学习布局检测、文本识别和关系理解，通过可扩展数据引擎合成多语言语料。
- 在OmniDocBench上达到SOTA性能，在XDocParse基准上领先次优方法7.4分，验证其多语言能力。

## 摘要（原文）

> Document Layout Parsing serves as a critical gateway for Artificial Intelligence (AI) to access and interpret the world's vast stores of structured knowledge. This process,which encompasses layout detection, text recognition, and relational understanding, is particularly crucial for empowering next-generation Vision-Language Models. Current methods, however, rely on fragmented, multi-stage pipelines that suffer from error propagation and fail to leverage the synergies of joint training. In this paper, we introduce dots.ocr, a single Vision-Language Model that, for the first time, demonstrates the advantages of jointly learning three core tasks within a unified, end-to-end framework. This is made possible by a highly scalable data engine that synthesizes a vast multilingual corpus, empowering the model to deliver robust performance across a wide array of tasks, encompassing diverse languages, layouts, and domains. The efficacy of our unified paradigm is validated by state-of-the-art performance on the comprehensive OmniDocBench. Furthermore, to catalyze research in global document intelligence, we introduce XDocParse, a challenging new benchmark spanning 126 languages. On this testbed, dots.ocr establishes a powerful new baseline, outperforming the next-best competitor by a remarkable +7.4 point margin and proving its unparalleled multilingual capabilities.

