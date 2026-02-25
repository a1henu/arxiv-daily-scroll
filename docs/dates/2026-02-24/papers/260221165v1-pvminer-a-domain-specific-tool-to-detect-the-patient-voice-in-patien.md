---
layout: default
title: PVminer: A Domain-Specific Tool to Detect the Patient Voice in Patient Generated Data
---

# PVminer: A Domain-Specific Tool to Detect the Patient Voice in Patient Generated Data
**arXiv**：[2602.21165v1](https://arxiv.org/abs/2602.21165) · [PDF](https://arxiv.org/pdf/2602.21165.pdf)  
**作者**：Samah Fodeh, Linhai Ma, Yan Wang, Srivani Talakokkul, Ganesh Puthiaraju, Afshan Khan, Ashley Hagaman, Sarah Lowe, Aimee Roundtree  

**一句话要点**：提出PVminer以结构化检测患者生成数据中的患者声音，集成领域适应BERT与主题建模。

**关键词**：患者声音检测, 自然语言处理, 领域适应BERT, 多标签分类, 主题建模, 医疗文本分析

## 3 点简述
- 核心问题：传统定性编码劳动密集，现有ML/NLP方法未充分整合患者中心沟通与社会健康决定因素。
- 方法要点：采用多标签多类预测，结合患者特定BERT编码器、无监督主题建模增强语义输入。
- 实验或效果：在分层任务中表现优异，F1分数达82.25%（Code），优于生物医学和临床预训练基线。

## 摘要（原文）

> Patient-generated text such as secure messages, surveys, and interviews contains rich expressions of the patient voice (PV), reflecting communicative behaviors and social determinants of health (SDoH). Traditional qualitative coding frameworks are labor intensive and do not scale to large volumes of patient-authored messages across health systems. Existing machine learning (ML) and natural language processing (NLP) approaches provide partial solutions but often treat patient-centered communication (PCC) and SDoH as separate tasks or rely on models not well suited to patient-facing language. We introduce PVminer, a domain-adapted NLP framework for structuring patient voice in secure patient-provider communication. PVminer formulates PV detection as a multi-label, multi-class prediction task integrating patient-specific BERT encoders (PV-BERT-base and PV-BERT-large), unsupervised topic modeling for thematic augmentation (PV-Topic-BERT), and fine-tuned classifiers for Code, Subcode, and Combo-level labels. Topic representations are incorporated during fine-tuning and inference to enrich semantic inputs. PVminer achieves strong performance across hierarchical tasks and outperforms biomedical and clinical pre-trained baselines, achieving F1 scores of 82.25% (Code), 80.14% (Subcode), and up to 77.87% (Combo). An ablation study further shows that author identity and topic-based augmentation each contribute meaningful gains. Pre-trained models, source code, and documentation will be publicly released, with annotated datasets available upon request for research use.

