---
layout: default
title: Unveiling and Bridging the Functional Perception Gap in MLLMs: Atomic Visual Alignment and Hierarchical Evaluation via PET-Bench
---

# Unveiling and Bridging the Functional Perception Gap in MLLMs: Atomic Visual Alignment and Hierarchical Evaluation via PET-Bench
**arXiv**：[2601.02737v1](https://arxiv.org/abs/2601.02737) · [PDF](https://arxiv.org/pdf/2601.02737.pdf)  
**作者**：Zanting Ye, Xiaolong Niu, Xuanbin Wu, Xu Han, Shengyuan Liu, Jing Hao, Zhihao Peng, Hao Sun, Jieqin Lv, Fanghu Wang, Yanchao Huang, Hubing Wu, Yixuan Yuan, Habib Zaidi, Arman Rahmim, Yefeng Zheng, Lijun Lu  

**一句话要点**：提出原子视觉对齐方法以解决多模态大语言模型在功能成像中的感知差距与思维链幻觉陷阱

**关键词**：多模态大语言模型, 功能成像, 原子视觉对齐, 思维链幻觉, PET-Bench基准, 医学影像分析

## 3 点简述
- 揭示当前视觉编码器在功能成像中无法独立于形态先验解码示踪剂生物分布的核心问题
- 提出原子视觉对齐微调策略，强制模型先掌握低层功能感知再进行高层诊断推理
- 通过PET-Bench基准评估19个先进模型，显示该方法将诊断准确率提升高达14.83%

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have demonstrated remarkable proficiency in tasks such as abnormality detection and report generation for anatomical modalities, their capability in functional imaging remains largely unexplored. In this work, we identify and quantify a fundamental functional perception gap: the inability of current vision encoders to decode functional tracer biodistribution independent of morphological priors. Identifying Positron Emission Tomography (PET) as the quintessential modality to investigate this disconnect, we introduce PET-Bench, the first large-scale functional imaging benchmark comprising 52,308 hierarchical QA pairs from 9,732 multi-site, multi-tracer PET studies. Extensive evaluation of 19 state-of-the-art MLLMs reveals a critical safety hazard termed the Chain-of-Thought (CoT) hallucination trap. We observe that standard CoT prompting, widely considered to enhance reasoning, paradoxically decouples linguistic generation from visual evidence in PET, producing clinically fluent but factually ungrounded diagnoses. To resolve this, we propose Atomic Visual Alignment (AVA), a simple fine-tuning strategy that enforces the mastery of low-level functional perception prior to high-level diagnostic reasoning. Our results demonstrate that AVA effectively bridges the perception gap, transforming CoT from a source of hallucination into a robust inference tool and improving diagnostic accuracy by up to 14.83%. Code and data are available at https://github.com/yezanting/PET-Bench.

