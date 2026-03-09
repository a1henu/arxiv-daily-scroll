---
layout: default
title: TumorChain: Interleaved Multimodal Chain-of-Thought Reasoning for Traceable Clinical Tumor Analysis
---

# TumorChain: Interleaved Multimodal Chain-of-Thought Reasoning for Traceable Clinical Tumor Analysis
**arXiv**：[2603.05867v1](https://arxiv.org/abs/2603.05867) · [PDF](https://arxiv.org/pdf/2603.05867.pdf)  
**作者**：Sijing Li, Zhongwei Qiu, Jiang Liu, Wenqiao Zhang, Tianwei Lin, Yihan Xie, Jianxiang An, Boxiang Yun, Chenglin Yang, Jun Xiao, Guangyu Guo, Jiawen Yao, Wei Liu, Yuan Gao, Ke Yan, Weiwei Cao, Zhilin Zheng, Tony C. W. Mok, Kai Cao, Yu Shi, Jiuyu Zhang, Jian Zhou, Beng Chin Ooi, Yingda Xia, Ling Zhang  

**一句话要点**：提出TumorChain多模态交错推理框架，用于可追溯的临床肿瘤分析

**关键词**：多模态推理, 临床肿瘤分析, 链式思维, 医学影像理解, 可解释人工智能

## 3 点简述
- 针对临床肿瘤分析任务，构建大规模多模态推理基准TumorCoT数据集
- 提出TumorChain框架，通过跨模态对齐和交错因果推理实现证据追溯
- 实验在病灶检测、印象生成和病理分类上优于基线，并展示良好泛化能力

## 摘要（原文）

> Accurate tumor analysis is central to clinical radiology and precision oncology, where early detection, reliable lesion characterization, and pathology-level risk assessment guide diagnosis and treatment planning. Chain-of-Thought (CoT) reasoning is particularly important in this setting because it enables step-by-step interpretation from imaging findings to clinical impressions and pathology conclusions, improving traceability and reducing diagnostic errors. Here, we target the clinical tumor analysis task and build a large-scale benchmark that operationalizes a multimodal reasoning pipeline, spanning findings, impressions, and pathology predictions. We curate TumorCoT, a large-scale dataset of 1.5M CoT-labeled VQA instructions paired with 3D CT scans, with step-aligned rationales and cross-modal alignments along the trajectory from findings to impression to pathology, enabling evaluation of both answer accuracy and reasoning consistency. We further propose TumorChain, a multimodal interleaved reasoning framework that tightly couples 3D imaging encoders, clinical text understanding, and organ-level vision-language alignment. Through cross-modal alignment and iterative interleaved causal reasoning, TumorChain grounds visual evidence, aggregates conclusions, and issues pathology predictions after multiple rounds of self-refinement, improving traceability and reducing hallucination risk. Experiments show consistent improvements over strong baselines in lesion detection, impression generation, and pathology classification, and demonstrate strong generalization on the DeepTumorVQA benchmark. These results highlight the potential of multimodal reasoning for reliable and interpretable tumor analysis in clinical practice. Detailed information about our project can be found on our project homepage at https://github.com/ZJU4HealthCare/TumorChain.

