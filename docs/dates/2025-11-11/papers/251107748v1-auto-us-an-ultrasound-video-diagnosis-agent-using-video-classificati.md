---
layout: default
title: Auto-US: An Ultrasound Video Diagnosis Agent Using Video Classification Framework and LLMs
---

# Auto-US: An Ultrasound Video Diagnosis Agent Using Video Classification Framework and LLMs
**arXiv**：[2511.07748v1](https://arxiv.org/abs/2511.07748) · [PDF](https://arxiv.org/pdf/2511.07748.pdf)  
**作者**：Yuezhe Yang, Yiyue Guo, Wenjie Cai, Qingqing Ruan, Siying Wang, Xingbo Dong, Zhe Jin, Yong Dai  

**一句话要点**：提出Auto-US智能诊断代理，集成超声视频与临床文本以提升医疗影像分析效率。

**关键词**：超声视频诊断, 视频分类框架, 大语言模型, 临床文本集成, 智能诊断代理

## 3 点简述
- 核心问题：现有AI辅助超声视频诊断在数据集多样性、性能和临床适用性方面存在局限。
- 方法要点：开发CTU-Net实现超声视频分类，并整合大语言模型生成诊断建议。
- 实验或效果：在CUV数据集上准确率达86.73%，诊断评分超3/5，经临床验证有效。

## 摘要（原文）

> AI-assisted ultrasound video diagnosis presents new opportunities to enhance the efficiency and accuracy of medical imaging analysis. However, existing research remains limited in terms of dataset diversity, diagnostic performance, and clinical applicability. In this study, we propose \textbf{Auto-US}, an intelligent diagnosis agent that integrates ultrasound video data with clinical diagnostic text. To support this, we constructed \textbf{CUV Dataset} of 495 ultrasound videos spanning five categories and three organs, aggregated from multiple open-access sources. We developed \textbf{CTU-Net}, which achieves state-of-the-art performance in ultrasound video classification, reaching an accuracy of 86.73\% Furthermore, by incorporating large language models, Auto-US is capable of generating clinically meaningful diagnostic suggestions. The final diagnostic scores for each case exceeded 3 out of 5 and were validated by professional clinicians. These results demonstrate the effectiveness and clinical potential of Auto-US in real-world ultrasound applications. Code and data are available at: https://github.com/Bean-Young/Auto-US.

