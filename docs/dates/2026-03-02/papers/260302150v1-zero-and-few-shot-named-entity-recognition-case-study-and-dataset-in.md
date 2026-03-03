---
layout: default
title: Zero- and Few-Shot Named-Entity Recognition: Case Study and Dataset in the Crime Domain (CrimeNER)
---

# Zero- and Few-Shot Named-Entity Recognition: Case Study and Dataset in the Crime Domain (CrimeNER)
**arXiv**：[2603.02150v1](https://arxiv.org/abs/2603.02150) · [PDF](https://arxiv.org/pdf/2603.02150.pdf)  
**作者**：Miguel Lopez-Duran, Julian Fierrez, Aythami Morales, Daniel DeAlcala, Gonzalo Mancera, Javier Irigoyen, Ruben Tolosana, Oscar Delgado, Francisco Jurado, Alvaro Ortigosa  

**一句话要点**：提出CrimeNER案例研究与数据集，以解决犯罪领域零样本和少样本命名实体识别中数据缺乏问题。

**关键词**：命名实体识别, 零样本学习, 少样本学习, 犯罪领域数据集, 实体类型标注, 大型语言模型

## 3 点简述
- 核心问题：犯罪相关文档中缺乏足够标注数据，阻碍命名实体识别在执法机构中的应用。
- 方法要点：构建CrimeNERdb数据集，包含1.5k+标注文档，定义5种粗粒度实体和22种细粒度实体类型。
- 实验或效果：在零样本和少样本设置下，使用最先进NER模型和大型语言模型评估数据质量和案例研究效果。

## 摘要（原文）

> The extraction of critical information from crime-related documents is a crucial task for law enforcement agencies. Named-Entity Recognition (NER) can perform this task in extracting information about the crime, the criminal, or law enforcement agencies involved. However, there is a considerable lack of adequately annotated data on general real-world crime scenarios. To address this issue, we present CrimeNER, a case-study of Crime-related zero- and Few-Shot NER, and a general Crime-related Named-Entity Recognition database (CrimeNERdb) consisting of more than 1.5k annotated documents for the NER task extracted from public reports on terrorist attacks and the U.S. Department of Justice's press notes. We define 5 types of coarse crime entity and a total of 22 types of fine-grained entity. We address the quality of the case-study and the annotated data with experiments on Zero and Few-Shot settings with State-of-the-Art NER models as well as generalist and commonly used Large Language Models.

