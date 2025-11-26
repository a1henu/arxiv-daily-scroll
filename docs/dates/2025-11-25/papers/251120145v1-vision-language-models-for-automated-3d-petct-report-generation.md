---
layout: default
title: Vision-Language Models for Automated 3D PET/CT Report Generation
---

# Vision-Language Models for Automated 3D PET/CT Report Generation
**arXiv**：[2511.20145v1](https://arxiv.org/abs/2511.20145) · [PDF](https://arxiv.org/pdf/2511.20145.pdf)  
**作者**：Wenpei Jiao, Kun Shang, Hui Li, Ke Yan, Jiajin Zhang, Guangjie Yang, Lijuan Guo, Yan Wan, Xing Yang, Dakai Jin, Zhaoheng Xie  

**一句话要点**：提出PETRG-3D框架以解决PET/CT自动报告生成中的3D上下文和医院间风格差异问题

**关键词**：PET/CT报告生成, 3D视觉语言模型, 多模态医学影像, 风格自适应提示, 淋巴瘤数据集

## 3 点简述
- 核心问题：PET/CT报告生成面临代谢模式多变和3D上下文需求，且医院间报告风格差异大
- 方法要点：采用端到端3D双分支框架，分别编码PET和CT体积，并引入风格自适应提示
- 实验或效果：在自然语言和临床指标上显著优于现有方法，如ROUGE-L提升31.49%

## 摘要（原文）

> Positron emission tomography/computed tomography (PET/CT) is essential in oncology, yet the rapid expansion of scanners has outpaced the availability of trained specialists, making automated PET/CT report generation (PETRG) increasingly important for reducing clinical workload. Compared with structural imaging (e.g., X-ray, CT, and MRI), functional PET poses distinct challenges: metabolic patterns vary with tracer physiology, and whole-body 3D contextual information is required rather than local-region interpretation. To advance PETRG, we propose PETRG-3D, an end-to-end 3D dual-branch framework that separately encodes PET and CT volumes and incorporates style-adaptive prompts to mitigate inter-hospital variability in reporting practices. We construct PETRG-Lym, a multi-center lymphoma dataset collected from four hospitals (824 reports w/ 245,509 paired PET/CT slices), and construct AutoPET-RG-Lym, a publicly accessible PETRG benchmark derived from open imaging data but equipped with new expert-written, clinically validated reports (135 cases). To assess clinical utility, we introduce PETRG-Score, a lymphoma-specific evaluation protocol that jointly measures metabolic and structural findings across curated anatomical regions. Experiments show that PETRG-3D substantially outperforms existing methods on both natural language metrics (e.g., +31.49\% ROUGE-L) and clinical efficacy metrics (e.g., +8.18\% PET-All), highlighting the benefits of volumetric dual-modality modeling and style-aware prompting. Overall, this work establishes a foundation for future PET/CT-specific models emphasizing disease-aware reasoning and clinically reliable evaluation. Codes, models, and AutoPET-RG-Lym will be released.

