---
layout: default
title: From Lemmas to Dependencies: What Signals Drive Light Verbs Classification?
---

# From Lemmas to Dependencies: What Signals Drive Light Verbs Classification?
**arXiv**：[2602.04127v1](https://arxiv.org/abs/2602.04127) · [PDF](https://arxiv.org/pdf/2602.04127.pdf)  
**作者**：Sercan Karakaş, Yusuf Şimşek  

**一句话要点**：通过限制模型输入探究土耳其语轻动词构式分类的信号驱动因素。

**关键词**：轻动词构式, 土耳其语处理, 多词表达分类, 词元归一化, 语法特征分析, 诊断评估

## 3 点简述
- 核心问题：土耳其语中轻动词构式分类受何种信号驱动，尤其在形态丰富和复杂谓词背景下。
- 方法要点：系统比较词元驱动、语法驱动和全输入基线模型，使用UD监督和诊断集评估。
- 实验或效果：发现粗粒度语法不足以稳健检测，词元身份支持分类但依赖归一化操作。

## 摘要（原文）

> Light verb constructions (LVCs) are a challenging class of verbal multiword expressions, especially in Turkish, where rich morphology and productive complex predicates create minimal contrasts between idiomatic predicate meanings and literal verb--argument uses. This paper asks what signals drive LVC classification by systematically restricting model inputs. Using UD-derived supervision, we compare lemma-driven baselines (lemma TF--IDF + Logistic Regression; BERTurk trained on lemma sequences), a grammar-only Logistic Regression over UD morphosyntax (UPOS/DEPREL/MORPH), and a full-input BERTurk baseline. We evaluate on a controlled diagnostic set with Random negatives, lexical controls (NLVC), and LVC positives, reporting split-wise performance to expose decision-boundary behavior. Results show that coarse morphosyntax alone is insufficient for robust LVC detection under controlled contrasts, while lexical identity supports LVC judgments but is sensitive to calibration and normalization choices. Overall, Our findings motivate targeted evaluation of Turkish MWEs and show that ``lemma-only'' is not a single, well-defined representation, but one that depends critically on how normalization is operationalized.

