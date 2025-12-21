---
layout: default
title: A multi-centre, multi-device benchmark dataset for landmark-based comprehensive fetal biometry
---

# A multi-centre, multi-device benchmark dataset for landmark-based comprehensive fetal biometry
**arXiv**：[2512.16710v1](https://arxiv.org/abs/2512.16710) · [PDF](https://arxiv.org/pdf/2512.16710.pdf)  
**作者**：Chiara Di Vece, Zhehua Mao, Netanell Avisdris, Brian Dromey, Raffaele Napolitano, Dafna Ben Bashat, Francisco Vasconcelos, Danail Stoyanov, Leo Joskowicz, Sophia Bano  

**一句话要点**：提出首个公开多中心多设备胎儿超声基准数据集，以解决胎儿生物测量中领域适应与泛化问题。

**关键词**：胎儿超声生物测量, 多中心数据集, 领域适应, 基准评估, 人工智能辅助诊断, 医学图像分析

## 3 点简述
- 核心问题：胎儿超声生物测量依赖手动标注，存在耗时、操作者依赖性和跨设备中心变异性，限制自动化方法可重复性。
- 方法要点：提供包含4,513张图像、1,904名受试者的多中心多设备数据集，涵盖主要生物测量指标，并附标准化训练/测试分割与评估代码。
- 实验或效果：通过自动生物测量模型量化领域偏移，显示单中心训练评估会高估性能，强调多中心测试的重要性。

## 摘要（原文）

> Accurate fetal growth assessment from ultrasound (US) relies on precise biometry measured by manually identifying anatomical landmarks in standard planes. Manual landmarking is time-consuming, operator-dependent, and sensitive to variability across scanners and sites, limiting the reproducibility of automated approaches. There is a need for multi-source annotated datasets to develop artificial intelligence-assisted fetal growth assessment methods. To address this bottleneck, we present an open, multi-centre, multi-device benchmark dataset of fetal US images with expert anatomical landmark annotations for clinically used fetal biometric measurements. These measurements include head bi-parietal and occipito-frontal diameters, abdominal transverse and antero-posterior diameters, and femoral length. The dataset contains 4,513 de-identified US images from 1,904 subjects acquired at three clinical sites using seven different US devices. We provide standardised, subject-disjoint train/test splits, evaluation code, and baseline results to enable fair and reproducible comparison of methods. Using an automatic biometry model, we quantify domain shift and demonstrate that training and evaluation confined to a single centre substantially overestimate performance relative to multi-centre testing. To the best of our knowledge, this is the first publicly available multi-centre, multi-device, landmark-annotated dataset that covers all primary fetal biometry measures, providing a robust benchmark for domain adaptation and multi-centre generalisation in fetal biometry and enabling more reliable AI-assisted fetal growth assessment across centres. All data, annotations, training code, and evaluation pipelines are made publicly available.

