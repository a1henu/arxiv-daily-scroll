---
layout: default
title: Inter-patient ECG Arrhythmia Classification with LGNs and LUTNs
---

# Inter-patient ECG Arrhythmia Classification with LGNs and LUTNs
**arXiv**：[2601.11433v1](https://arxiv.org/abs/2601.11433) · [PDF](https://arxiv.org/pdf/2601.11433.pdf)  
**作者**：Wout Mommen, Lars Keuninckx, Paul Detterer, Achiel Colpaert, Piet Wambacq  

**一句话要点**：提出基于LGNs和LUTNs的ECG心律失常分类方法，用于低功耗可穿戴设备中的跨患者检测。

**关键词**：心电图分类, 低功耗神经网络, 跨患者范式, 可穿戴设备, MIT-BIH数据集, FPGA实现

## 3 点简述
- 核心问题：跨患者ECG心律失常自动分类，适用于心脏植入物或可穿戴设备。
- 方法要点：使用LGNs和LUTNs，结合新型预处理和MUX训练方法，实现极低计算开销。
- 实验或效果：在MIT-BIH数据集上达到94.28%准确率，功耗低至5-7 mW，计算量减少3-6个数量级。

## 摘要（原文）

> Deep Differentiable Logic Gate Networks (LGNs) and Lookup Table Networks (LUTNs) are demonstrated to be suitable for the automatic classification of electrocardiograms (ECGs) using the inter-patient paradigm. The methods are benchmarked using the MIT-BIH arrhythmia data set, achieving up to 94.28% accuracy and a $jκ$ index of 0.683 on a four-class classification problem. Our models use between 2.89k and 6.17k FLOPs, including preprocessing and readout, which is three to six orders of magnitude less compared to SOTA methods. A novel preprocessing method is utilized that attains superior performance compared to existing methods for both the mixed-patient and inter-patient paradigms. In addition, a novel method for training the Lookup Tables (LUTs) in LUTNs is devised that uses the Boolean equation of a multiplexer (MUX). Additionally, rate coding was utilized for the first time in these LGNs and LUTNs, enhancing the performance of LGNs. Furthermore, it is the first time that LGNs and LUTNs have been benchmarked on the MIT-BIH arrhythmia dataset using the inter-patient paradigm. Using an Artix 7 FPGA, between 2000 and 2990 LUTs were needed, and between 5 to 7 mW (i.e. 50 pJ to 70 pJ per inference) was estimated for running these models. The performance in terms of both accuracy and $jκ$-index is significantly higher compared to previous LGN results. These positive results suggest that one can utilize LGNs and LUTNs for the detection of arrhythmias at extremely low power and high speeds in heart implants or wearable devices, even for patients not included in the training set.

