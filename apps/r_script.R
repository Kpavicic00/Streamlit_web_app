lige <- read.csv("/home/dule/Desktop/Legit_apps/Football_data_revolution/test_data.csv")
colnames(lige) <- c("Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION")

g3 <- ggplot(lige, aes(Year)) +
  geom_smooth(aes(y = Expend_by_player, colour = "Expenditure without inflation"),lwd = 2, se = F) +
  geom_smooth(aes(y = Expend_INFLACION, colour = "Expenditure with inflation"),lwd = 2, se = F) +
  scale_colour_manual(values = c("orange4", "cyan4"))+
  scale_y_continuous(" Expend ",labels = scales::comma)+
  scale_x_continuous(" Year ")+
  labs(title = "Expenditure with inflation and without inflation",caption="Transfmarket.com",color = " Consumption\n")

g3 + theme( axis.title=element_text(size=17,face="bold",color = "gray16"),
            axis.text = element_text(face = "bold", size = 17,color = "gray16"),
            plot.title = element_text(size = 20, face = "italic",color = "gray16"))