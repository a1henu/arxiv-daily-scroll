---
layout: default
title: Transcriptome-Conditioned Personalized De Novo Drug Generation for AML Using Metaheuristic Assembly and Target-Driven Filtering
---

# Transcriptome-Conditioned Personalized De Novo Drug Generation for AML Using Metaheuristic Assembly and Target-Driven Filtering
**arXiv**：[2512.21301v1](https://arxiv.org/abs/2512.21301) · [PDF](https://arxiv.org/pdf/2512.21301.pdf)  
**作者**：Abdullah G. Elafifi, Basma Mamdouh, Mariam Hanafy, Muhammed Alaa Eldin, Yosef Khaled, Nesma Mohamed El-Gelany, Tarek H. M. Abou-El-Enien  

**一句话要点**：提出基于转录组和元启发式组装的个性化从头药物生成框架以解决AML精准治疗难题

**关键词**：急性髓系白血病, 从头药物生成, 元启发式算法, 转录组学, 分子对接, 精准医学

## 3 点简述
- 核心问题：AML分子异质性高，现有精准疗法覆盖不足，需个性化药物发现。
- 方法要点：利用WGCNA识别生物标志物，结合AlphaFold3建模和DOGSiteScorer定位热点，开发反应优先元启发式算法组装新配体。
- 实验或效果：生成药物样化学实体，通过ADMET和分子对接验证，如Ligand L1结合自由能为-6.571 kcal/mol。

## 摘要（原文）

> Acute Myeloid Leukemia (AML) remains a clinical challenge due to its extreme molecular heterogeneity and high relapse rates. While precision medicine has introduced mutation-specific therapies, many patients still lack effective, personalized options. This paper presents a novel, end-to-end computational framework that bridges the gap between patient-specific transcriptomics and de novo drug discovery. By analyzing bulk RNA sequencing data from the TCGA-LAML cohort, the study utilized Weighted Gene Co-expression Network Analysis (WGCNA) to prioritize 20 high-value biomarkers, including metabolic transporters like HK3 and immune-modulatory receptors such as SIGLEC9. The physical structures of these targets were modeled using AlphaFold3, and druggable hotspots were quantitatively mapped via the DOGSiteScorer engine. Then developed a novel, reaction-first evolutionary metaheuristic algorithm as well as multi-objective optimization programming that assembles novel ligands from fragment libraries, guided by spatial alignment to these identified hotspots. The generative model produced structurally unique chemical entities with a strong bias toward drug-like space, as evidenced by QED scores peaking between 0.5 and 0.7. Validation through ADMET profiling and SwissDock molecular docking identified high-confidence candidates, such as Ligand L1, which achieved a binding free energy of -6.571 kcal/mol against the A08A96 biomarker. These results demonstrate that integrating systems biology with metaheuristic molecular assembly can produce pharmacologically viable, patient tailored leads, offering a scalable blueprint for precision oncology in AML and beyond

