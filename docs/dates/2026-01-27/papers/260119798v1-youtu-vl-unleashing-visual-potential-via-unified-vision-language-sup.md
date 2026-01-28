---
layout: default
title: Youtu-VL: Unleashing Visual Potential via Unified Vision-Language Supervision
---

# Youtu-VL: Unleashing Visual Potential via Unified Vision-Language Supervision
**arXiv**：[2601.19798v1](https://arxiv.org/abs/2601.19798) · [PDF](https://arxiv.org/pdf/2601.19798.pdf)  
**作者**：Zhixiang Wei, Yi Li, Zhehan Kan, Xinghua Jiang, Zuwei Long, Shifeng Liu, Hongze Shen, Wei Liu, Xiaoyu Tan, Haojia Lin, Yubo Zhu, Qianyu Li, Di Yin, Haoyu Cao, Weibo Gu, Xin Li, Yinsong Liu, Deqiang Jiang, Xing Sun, Yunsheng Wu, Mingkong Tang, Shuangyin Liu, Lexiang Tang, Haodong Lin, Junru Lu, Jiarui Qin, Lingfeng Qiao, Ruizhi Qiao, Bo Ke, Jianfeng He, Ke Li, Yangning Li, Yunhang Shen, Mengdan Zhang, Peixian Chen, Kun Yin, Bing Liu, Yunfei Wu, Huang Chen, Zhongpeng Cai, Xiaotian Li  

**一句话要点**：提出Youtu-VL框架，通过统一视觉-语言自回归监督解决视觉语言模型中视觉信息保留不足的问题。

**关键词**：视觉语言模型, 自回归监督, 多模态理解, 视觉中心任务, 统一监督范式

## 3 点简述
- 核心问题：当前视觉语言模型存在文本主导优化偏差，导致视觉信息保留不足，影响多模态理解。
- 方法要点：引入视觉-语言统一自回归监督范式，将视觉信号作为预测目标而非条件输入，实现视觉与语言的统一监督。
- 实验或效果：在通用多模态任务和视觉中心任务上表现竞争性，为通用视觉代理奠定基础。

## 摘要（原文）

> Despite the significant advancements represented by Vision-Language Models (VLMs), current architectures often exhibit limitations in retaining fine-grained visual information, leading to coarse-grained multimodal comprehension. We attribute this deficiency to a suboptimal training paradigm inherent in prevailing VLMs, which exhibits a text-dominant optimization bias by conceptualizing visual signals merely as passive conditional inputs rather than supervisory targets. To mitigate this, we introduce Youtu-VL, a framework leveraging the Vision-Language Unified Autoregressive Supervision (VLUAS) paradigm, which fundamentally shifts the optimization objective from ``vision-as-input'' to ``vision-as-target.'' By integrating visual tokens directly into the prediction stream, Youtu-VL applies unified autoregressive supervision to both visual details and linguistic content. Furthermore, we extend this paradigm to encompass vision-centric tasks, enabling a standard VLM to perform vision-centric tasks without task-specific additions. Extensive empirical evaluations demonstrate that Youtu-VL achieves competitive performance on both general multimodal tasks and vision-centric tasks, establishing a robust foundation for the development of comprehensive generalist visual agents.

