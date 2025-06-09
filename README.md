# Data-Mining-HW2 🪄 | Time Series Anomaly Detection Toolkit

Python · PyPI · TSLib · Autoformer · FEDformer · TimesNet

一个示例仓库，展示如何基于 [TSLib](https://github.com/thuml/Time-Series-Library) 的 Autoformer、FEDformer 和 TimesNet 模型完成时序数据的异常检测、评估与可视化。

---

## 📂 Repository Layout

| 路径／文件                                 | 说明                                                      | 涉及技术                                                          |
|-----------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------|
| `data/`                                 | 原始与标签数据                                            | CSV 时序特征 & 二分类标签                                         |
| `data_provider/`                        | 数据集加载与工厂                                          | M4、UEA、Tube 等不同数据源的封装                                |
| `exp/`                                  | 各任务实验入口                                          | `exp_anomaly_detection.py`（异常检测）、`exp_basic.py` 等     |
| `layers/`                               | 自定义网络层                                            | 时间序列模型的核心组件                                          |
| `models/`                               | 模型定义                                                | Autoformer、FEDformer、TimesNet                                 |
| `scripts/anomaly_detection/Tube/`       | 一键运行脚本                                             | `Autoformer_Tube.sh`、`FEDformer_Tube.sh`、`TimesNet_Tube.sh` |
| `utils/`                                | 辅助函数                                                | 日志、可视化、指标计算                                          |
| `run.py` / `total.py`                   | 命令行入口                                              | 支持 `--task`、`--model`、`--dataset` 等参数                     |
| `result_anomaly_detection.txt`          | 演示输出                                                | Precision/Recall/F1 等                                        |
| `requirements.txt`                      | Python 依赖                                              | PyTorch, NumPy, Pandas, Matplotlib, TSLib 等                    |
| `README.md`                             | 项目说明                                                | —                                                               |

---

## 🚀 Features

- 🔹 **Autoformer**：滑动窗口级别的时序异常检测  
- 🔹 **FEDformer**：频域增强的时序异常检测  
- 🔹 **TimesNet**：二维时序特征提取与异常检测  
- 🔹 自动计算并输出 **Accuracy**, **Precision**, **Recall**, **F1-score**  
- 🔹 绘制并保存异常点可视化图表  

---

## 🛠 Tech Stack

- **语言**：Python 3.8+  
- **深度学习框架**：PyTorch  
- **时序分析库**：TSLib  
- **数据处理**：NumPy、Pandas  
- **可视化**：Matplotlib  

---

## 🚀 Quick Start

1. **克隆仓库**
   ```bash
   git clone https://github.com/htupeilrahc/Data-Mining-HW2.git
   cd Data-Mining-HW2

2. **安装依赖**
   ```bash
   pip install -r requirements.txt

3. **运行实验**
   ```bash
   bash scripts/anomaly_detection/Tube/Autoformer_Tube.sh

4.**运行实验**

## 📖 Reference
如果在学术工作中使用本项目或其组件，请引用：
  ```bash
@inproceedings{wu2023timesnet,
  title     = {TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis},
  author    = {Haixu Wu and Tengge Hu and Yong Liu and Hang Zhou and Jianmin Wang and Mingsheng Long},
  booktitle = {International Conference on Learning Representations},
  year      = {2023},
}
@inproceedings{zhou2022fedformer,
  title     = {FEDformer: Frequency Enhanced Decomposed Transformer for Long-term Series Forecasting},
  author    = {Hang Zhou and Minghan Li and Zhen Cui and Yujuan Han and Mingsheng Long},
  booktitle = {ICML},
  year      = {2022},
}
@inproceedings{wu2021autoformer,
  title     = {Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting},
  author    = {Zhenguo Li and Haixu Wu and Xinyu Wu and Mingsheng Long},
  booktitle = {NeurIPS},
  year      = {2021},
}

##🙏 Acknowledgements
-感谢 TSLib 团队提供的 Autoformer、FEDformer 与 TimesNet 实现
