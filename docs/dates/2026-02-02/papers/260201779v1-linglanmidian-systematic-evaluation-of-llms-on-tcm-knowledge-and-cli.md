---
layout: default
title: LingLanMiDian: Systematic Evaluation of LLMs on TCM Knowledge and Clinical Reasoning
---

# LingLanMiDian: Systematic Evaluation of LLMs on TCM Knowledge and Clinical Reasoning
**arXiv**：[2602.01779v1](https://arxiv.org/abs/2602.01779) · [PDF](https://arxiv.org/pdf/2602.01779.pdf)  
**作者**：Rui Hua, Yu Wei, Zixin Shu, Kai Chang, Dengying Yan, Jianan Xia, Zeyu Liu, Hui Zhu, Shujie Song, Mingzhong Xiao, Xiaodong Li, Dongmei Jia, Zhuye Gao, Yanyan Meng, Naixuan Zhao, Yu Fu, Haibin Yu, Benman Yu, Yuanyuan Chen, Fei Dong, Zhizhou Meng, Pengcheng Yang, Songxue Zhao, Lijuan Pei, Yunhui Hu, Kan Ding, Jiayuan Duan, Wenmao Yin, Yang Gu, Runshun Zhang, Qiang Zhu, Jian Yu, Jiansheng Li, Baoyan Liu, Wenjia Wang, Xuezhong Zhou  

**一句话要点**：提出LingLanMiDian基准以系统评估大语言模型在中医知识与临床推理中的表现

**关键词**：中医自然语言处理, 大语言模型评估, 临床决策支持, 多任务基准, 零-shot学习, 知识推理

## 3 点简述
- 现有中医基准覆盖碎片化且评分不统一，阻碍公平比较
- LingLan引入统一多任务评估、同义词容忍协议和硬子集设计
- 零-shot评估14个模型，揭示在中医专业推理上与专家的差距

## 摘要（原文）

> Large language models (LLMs) are advancing rapidly in medical NLP, yet Traditional Chinese Medicine (TCM) with its distinctive ontology, terminology, and reasoning patterns requires domain-faithful evaluation. Existing TCM benchmarks are fragmented in coverage and scale and rely on non-unified or generation-heavy scoring that hinders fair comparison. We present the LingLanMiDian (LingLan) benchmark, a large-scale, expert-curated, multi-task suite that unifies evaluation across knowledge recall, multi-hop reasoning, information extraction, and real-world clinical decision-making. LingLan introduces a consistent metric design, a synonym-tolerant protocol for clinical labels, a per-dataset 400-item Hard subset, and a reframing of diagnosis and treatment recommendation into single-choice decision recognition. We conduct comprehensive, zero-shot evaluations on 14 leading open-source and proprietary LLMs, providing a unified perspective on their strengths and limitations in TCM commonsense knowledge understanding, reasoning, and clinical decision support; critically, the evaluation on Hard subset reveals a substantial gap between current models and human experts in TCM-specialized reasoning. By bridging fundamental knowledge and applied reasoning through standardized evaluation, LingLan establishes a unified, quantitative, and extensible foundation for advancing TCM LLMs and domain-specific medical AI research. All evaluation data and code are available at https://github.com/TCMAI-BJTU/LingLan and http://tcmnlp.com.

