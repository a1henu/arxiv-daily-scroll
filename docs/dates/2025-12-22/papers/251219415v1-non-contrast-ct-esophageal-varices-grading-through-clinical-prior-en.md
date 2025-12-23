---
layout: default
title: Non-Contrast CT Esophageal Varices Grading through Clinical Prior-Enhanced Multi-Organ Analysis
---

# Non-Contrast CT Esophageal Varices Grading through Clinical Prior-Enhanced Multi-Organ Analysis
**arXiv**：[2512.19415v1](https://arxiv.org/abs/2512.19415) · [PDF](https://arxiv.org/pdf/2512.19415.pdf)  
**作者**：Xiaoming Zhang, Chunli Li, Jiacheng Hao, Yuan Gao, Danyang Tu, Jianyi Qiao, Xiaoli Yin, Le Lu, Ling Zhang, Ke Yan, Yang Hou, Yu Shi  

**一句话要点**：提出MOON++框架，通过多器官分析增强非对比CT食管静脉曲张分级

**关键词**：非对比CT, 食管静脉曲张分级, 多器官分析, 临床先验增强, 多模态学习, 非侵入性诊断

## 3 点简述
- 核心问题：食管静脉曲张传统依赖侵入性内镜诊断，非对比CT作为非侵入性替代方法未充分利用。
- 方法要点：MOON++结合临床先验知识，通过多模态学习综合分析食管、肝脏和脾脏的影像特征。
- 实验或效果：在1631名患者数据上验证，MOON++在严重分级任务中AUC达0.894，优于单器官方法。

## 摘要（原文）

> Esophageal varices (EV) represent a critical complication of portal hypertension, affecting approximately 60% of cirrhosis patients with a significant bleeding risk of ~30%. While traditionally diagnosed through invasive endoscopy, non-contrast computed tomography (NCCT) presents a potential non-invasive alternative that has yet to be fully utilized in clinical practice. We present Multi-Organ-COhesion Network++ (MOON++), a novel multimodal framework that enhances EV assessment through comprehensive analysis of NCCT scans. Inspired by clinical evidence correlating organ volumetric relationships with liver disease severity, MOON++ synthesizes imaging characteristics of the esophagus, liver, and spleen through multimodal learning. We evaluated our approach using 1,631 patients, those with endoscopically confirmed EV were classified into four severity grades. Validation in 239 patient cases and independent testing in 289 cases demonstrate superior performance compared to conventional single organ methods, achieving an AUC of 0.894 versus 0.803 for the severe grade EV classification (G3 versus <G3) and 0.921 versus 0.793 for the differentiation of moderate to severe grades (>=G2 versus <G2). We conducted a reader study involving experienced radiologists to further validate the performance of MOON++. To our knowledge, MOON++ represents the first comprehensive multi-organ NCCT analysis framework incorporating clinical knowledge priors for EV assessment, potentially offering a promising non-invasive diagnostic alternative.

