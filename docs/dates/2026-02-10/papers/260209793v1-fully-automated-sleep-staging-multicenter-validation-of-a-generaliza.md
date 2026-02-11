---
layout: default
title: Fully-automated sleep staging: multicenter validation of a generalizable deep neural network for Parkinson's disease and isolated REM sleep behavior disorder
---

# Fully-automated sleep staging: multicenter validation of a generalizable deep neural network for Parkinson's disease and isolated REM sleep behavior disorder
**arXiv**：[2602.09793v1](https://arxiv.org/abs/2602.09793) · [PDF](https://arxiv.org/pdf/2602.09793.pdf)  
**作者**：Jesper Strøm, Casper Skjærbæk, Natasha Becker Bertelsen, Steffen Torpe Simonsen, Niels Okkels, David Bertram, Sinah Röttgen, Konstantin Kufer, Kaare B. Mikkelsen, Marit Otto, Poul Jørgen Jennum, Per Borghammer, Michael Sommerauer, Preben Kidmose  

**一句话要点**：提出基于U-Sleep的通用深度神经网络，用于帕金森病和孤立性REM睡眠行为障碍的自动睡眠分期

**关键词**：睡眠分期, 深度神经网络, 帕金森病, 孤立性REM睡眠行为障碍, 视频多导睡眠图, 模型微调

## 3 点简述
- 核心问题：手动睡眠分期在神经退行性疾病中因EEG异常和睡眠碎片化而困难，阻碍大规模RBD筛查。
- 方法要点：在大型公开非神经退行性数据集上预训练U-Sleep模型，并在PD和iRBD数据集上微调以提高泛化性。
- 实验或效果：微调后模型在独立数据集上κ值显著提升，置信度阈值优化使REM睡眠识别准确率从85%增至95.5%。

## 摘要（原文）

> Isolated REM sleep behavior disorder (iRBD) is a key prodromal marker of Parkinson's disease (PD), and video-polysomnography (vPSG) remains the diagnostic gold standard. However, manual sleep staging is particularly challenging in neurodegenerative diseases due to EEG abnormalities and fragmented sleep, making PSG assessments a bottleneck for deploying new RBD screening technologies at scale. We adapted U-Sleep, a deep neural network, for generalizable sleep staging in PD and iRBD. A pretrained U-Sleep model, based on a large publicly available, multisite non-neurodegenerative dataset (PUB; 19,236 PSGs across 12 sites), was fine-tuned on research datasets from two centers (Lundbeck Foundation Parkinson's Disease Research Center (PACE) and the Cologne-Bonn Cohort (CBC); 112 PD, 138 iRBD, 89 age-matched controls. The resulting model was evaluated on an independent dataset from the Danish Center for Sleep Medicine (DCSM; 81 PD, 36 iRBD, 87 sleep-clinic controls). A subset of PSGs with low agreement between the human rater and the model (\k{appa} < 0.6) was re-scored by a second blinded human rater to identify sources of disagreement. Finally, we applied confidence-based thresholds to optimize REM sleep staging. The pretrained model achieved mean \k{appa} = 0.81 in PUB, but \k{appa} = 0.66 when applied directly to PACE/CBC. By fine-tuning the model, we developed a generalized model with \k{appa} = 0.74 on PACE/CBC (p < 0.001 vs. the pretrained model). In DCSM, mean and median \k{appa} increased from 0.60 to 0.64 (p < 0.001) and 0.64 to 0.69 (p < 0.001), respectively. In the interrater study, PSGs with low agreement between the model and the initial scorer showed similarly low agreement between human scorers. Applying a confidence threshold increased the proportion of correctly identified REM sleep epochs from 85% to 95.5%, while preserving sufficient (> 5 min) REM sleep for 95% of subjects.

