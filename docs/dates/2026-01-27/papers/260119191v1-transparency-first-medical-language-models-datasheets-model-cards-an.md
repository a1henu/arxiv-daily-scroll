---
layout: default
title: Transparency-First Medical Language Models: Datasheets, Model Cards, and End-to-End Data Provenance for Clinical NLP
---

# Transparency-First Medical Language Models: Datasheets, Model Cards, and End-to-End Data Provenance for Clinical NLP
**arXiv**：[2601.19191v1](https://arxiv.org/abs/2601.19191) · [PDF](https://arxiv.org/pdf/2601.19191.pdf)  
**作者**：Olaf Yunus Laitinen Imanov, Taner Yilmaz, Ayse Tuba Tugrul, Melike Nesrin Zaman, Ozkan Gunalp, Duygu Erisken, Sila Burde Dulger, Rana Irem Turhan, Izzet Ozdemir, Derya Umut Kulali, Ozan Akbulut, Harun Demircioglu, Hasan Basri Kara, Berfin Tavan  

**一句话要点**：提出TeMLM透明优先发布框架，以增强临床语言模型的可追溯性与治理能力。

**关键词**：临床自然语言处理, 模型透明度, 数据溯源, 合成数据集, 可审计框架

## 3 点简述
- 核心问题：临床NLP模型缺乏统一、可审计的透明度标准，影响部署可靠性。
- 方法要点：定义TeMLM-Card、TeMLM-Datasheet和TeMLM-Provenance等机器可检查发布组件。
- 实验或效果：在Technetium-I合成数据集上验证ProtactiniumBERT模型，强调需真实数据验证。

## 摘要（原文）

> We introduce TeMLM, a set of transparency-first release artifacts for clinical language models. TeMLM unifies provenance, data transparency, modeling transparency, and governance into a single, machine-checkable release bundle. We define an artifact suite (TeMLM-Card, TeMLM-Datasheet, TeMLM-Provenance) and a lightweight conformance checklist for repeatable auditing. We instantiate the artifacts on Technetium-I, a large-scale synthetic clinical NLP dataset with 498,000 notes, 7.74M PHI entity annotations across 10 types, and ICD-9-CM diagnosis labels, and report reference results for ProtactiniumBERT (about 100 million parameters) on PHI de-identification (token classification) and top-50 ICD-9 code extraction (multi-label classification). We emphasize that synthetic benchmarks are valuable for tooling and process validation, but models should be validated on real clinical data prior to deployment.

